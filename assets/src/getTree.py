# do getfont2.py and getimg.py first
import sys
import os
import pandas as pd
import json
from time import sleep as sleep
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
class Crawler():

    def __init__(self):
        print(sys.platform)
        if sys.platform == "linux":
            chromedriver = 'driver/chromedriver-linux'
        else:
            chromedriver = 'driver/chromedriver.exe'
        if hasattr(sys, '_MEIPASS'):
            self.driver = os.path.join(sys._MEIPASS, chromedriver)
        else:
            self.driver = chromedriver
        
        self.browser = webdriver.Chrome(self.driver)
        self.mouse = webdriver.common.action_chains.ActionChains(self.browser)
        
        
        #self.tree = [["字體編號","衍生字"]]
        #self.tree = {"27.0000":["27.0000","27.0000","27.0000"]}
        self.tree = {}

        # self.browser.get('https://content.steeluniversity.org/simulators/bos/index.html')
        self.browser.get('http://xiaoxue.iis.sinica.edu.tw/ccdb?ccmapcode=4')
        print('web reached')
        sleep(10) #disable image showing on web manually
        
    def get_tree(self, thisfontid, thisfont):
        self.tree[thisfontid] = []
        self.browser.find_element_by_xpath('//*[@id="XiaozhuanParts"]').clear()
        self.browser.find_element_by_xpath('//*[@id="XiaozhuanParts"]').send_keys(thisfont)
        self.browser.find_element_by_xpath('//*[@id="Submit"]').click()
        sleep(2)
        page_info = self.browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/form/table[1]/tbody/tr/td').text
        page_info = page_info.split('／')[1].split('頁')[0]
        print("total pages: ", page_info)  
        for i in range(int(page_info)):
            print("parsing page: ", i+1)
            sleep(2)
            for tr_ in range(1, 11, 2):
                for td_ in range(1, 21, 2):
                    #xpath = '[@id="HiddenFrom"]/div/table/tbody/tr[' + str(tr_) + ']/td[' + str(td_) + ']/a'
                    xpath2 = '/html/body/table[2]/tbody/tr/td[3]/form/div/table/tbody/tr[' + str(tr_) + ']/td[' + str(td_) + ']/a'
                    #'/html/body/table[2]/tbody/tr/td[3]/form/div/table/tbody/tr[1]/td[3]/a'
                    try:
                        query = self.browser.find_element_by_xpath(xpath2)
                    except:
                        break
                        #print("cant")
                    #word
                    urlinfo = urlparse(query.get_attribute("href"))#.kaiOrder
                    #kai_order = parse_qs(urlinfo.query)['kaiOrder'][0]
                    #zh_order = query.text
                    
                    imgpath = '/html/body/table[2]/tbody/tr/td[3]/form/div/table/tbody/tr['+ str(tr_) + ']/td['+ str(td_) + ']/img'
                    imgele = self.browser.find_element_by_xpath(imgpath)
                    #print(imgele.get_attribute("src"))
                    urlinfo = urlparse(imgele.get_attribute("src"))
                    #print(urlinfo)
                    kai_txt = parse_qs(urlinfo.query)['text'][0]
                    #print(imgtxt)
                    kai_txt_bin = kai_txt.encode("utf-8")
                    #print(imgtxt_bin)
                    fontid = imgele.get_attribute("alt")[1:-1]
                    self.tree[thisfontid].append(fontid)
                    
            if (i + 1 != int(page_info)):
               self.browser.find_element_by_xpath('//*[@id="PageLink' + str(i + 2) + '"]').click()#change page
            
                    
crl = Crawler()
df = pd.read_csv('../db/dbimg.csv')
count = 1
thisfontid_map_font = pd.Series(df.楷書字型.values,index=df.字體編號).to_dict()
for k,v in thisfontid_map_font.items():
    print(k,v,count)
    crl.get_tree(k,v)
    
    with open('../db/dbtree.json', 'w') as f:
        json.dump(crl.tree, f)

    count += 1