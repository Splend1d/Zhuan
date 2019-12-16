# do getfont2.py and getimg.py first
import sys
import os
from time import sleep as sleep

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
        
        
        #self.tree = [["字體編號","衍生字","子部件"]]
        self.tree = {"27.0000":{"child":set(),"parent":set()}}

        # self.browser.get('https://content.steeluniversity.org/simulators/bos/index.html')
        self.browser.get('http://xiaoxue.iis.sinica.edu.tw/ccdb?ccmapcode=4')
        print('web reached')
        #sleep(10) #disable image showing on web manually
        
    def get_tree(self):
    	self.browser.find_element_by_xpath('//*[@id="XiaozhuanParts"]').send_keys("一")
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
                    kai_order = parse_qs(urlinfo.query)['kaiOrder'][0]
                    zh_order = query.text
                    
                    imgpath = '/html/body/table[2]/tbody/tr/td[3]/form/div/table/tbody/tr['+ str(tr_) + ']/td['+ str(td_) + ']/img'
                    imgele = self.browser.find_element_by_xpath(imgpath)
                    #print(imgele.get_attribute("src"))
                    urlinfo = urlparse(imgele.get_attribute("src"))
                    #print(urlinfo)
                    kai_txt = parse_qs(urlinfo.query)['text'][0]
                    #print(imgtxt)
                    kai_txt_bin = kai_txt.encode("utf-8")
                    #print(imgtxt_bin)
                    imgid = imgele.get_attribute("alt")[1:-1]
                    self.databasetxt.append([zh_order, kai_order, imgid, kai_txt, kai_txt_bin])
                    print(self.databasetxt)
                    s()
            if (i + 1 != int(page_info)):
               self.browser.find_element_by_xpath('//*[@id="PageLink' + str(i + 2) + '"]').click()#change page
            
                    
crl = Crawler()
crl.get_info()
with open('./db/db.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(crl.databasetxt)