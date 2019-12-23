import urllib.request
import urllib.parse
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
import json
import random
import sys
import os
from time import sleep as sleep
#import secondary

# a crawler class that handle all the crawling of webpages


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
        self.freq = 0
        self.enabled = False
        self.browser = webdriver.Chrome(self.driver)
        self.mouse = webdriver.common.action_chains.ActionChains(self.browser)
        # self.browser.get('https://content.steeluniversity.org/simulators/bos/index.html')
        self.browser.get('http://xiaoxue.iis.sinica.edu.tw/ccdb?ccmapcode=4')
        print('web reached')

    def q_draw(self, x):
        print("query: ", x)
        self.browser.find_element_by_xpath('//*[@id="KaishuStrokeCounts"]').send_keys(str(x))
        self.browser.find_element_by_xpath('//*[@id="Submit"]').click()
        sleep(2)
        page_info = self.browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/form/table[1]/tbody/tr/td').text
        page_info = page_info.split('／')[1].split('頁')[0]
        print("total pages: ", page_info)
        for i in range(int(page_info)):
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
                    #    print("cant")
                    ch_order = query.get_attribute("href").split('=')[-1]
                    kai_order = query.text
                    with open("database.txt", "a") as f:
                        f.write(ch_order + ',' + kai_order + ','+str(x)+'\n')
                    print(ch_order)
                    print(kai_order)
            if (i + 1 != int(page_info)):
                self.browser.find_element_by_xpath('//*[@id="PageLink' + str(i + 2) + '"]').click()
        self.browser.find_element_by_xpath('//*[@id="Reset"]').click()
        # self.browser.close()

    def get_info(self, query_list):
        with open("database_meaning.txt", "a",encoding = "utf-8") as f:
            for idx in query_list:
                self.browser.get("http://xiaoxue.iis.sinica.edu.tw/xiaozhuan?kaiOrder="+str(idx))
                while(True):
                    try:
                        n_results = self.browser.find_element_by_xpath('//*[@id="HiddenFrom"]/table/tbody/tr[2]/td').text
                        
                    except:
                        sleep(0.01)
                    else:
                        break
                print(n_results[4])
                if (n_results[4] == '0'):
                    none_p = ""
                    f.write('\t'.join([idx,none_p,none_p,none_p])+'\n')
                    continue
                meaning = self.browser.find_element_by_xpath('//*[@id="PageResult"]/dl/dd[1]').text
                pic_url = self.browser.find_element_by_xpath('//*[@id="HiddenFrom"]/table/tbody/tr[4]/td[1]/img').get_attribute("alt")
                location = self.browser.find_element_by_xpath('//*[@id="HiddenFrom"]/table/tbody/tr[4]/td[1]').text
                f.write('\t'.join([idx,meaning,location,pic_url])+'\n')

    

    def get_image(self, query_list):
        pass
    #   bad method archived
    #     count = 0
    #     for c in query_list:
    #         c_uni=c[0].encode("utf-8")
    #         #print(c_uni)
    #         translated = ""
    #         for b in c_uni:
    #             translated = translated + '%'+str(hex(b))[2:]
    #         #print(translated)
    #         url = "http://xiaoxue.iis.sinica.edu.tw/ImageText2/ShowImage.ashx?text="+translated+"&font=%e5%8c%97%e5%b8%ab%e5%a4%a7%e8%aa%aa%e6%96%87%e5%b0%8f%e7%af%86&size=400&style=regular&color=%23000000"
            
    #         #url = u"http://xiaoxue.iis.sinica.edu.tw/ImageText2/ShowImage.ashx?text="+c[0]+"&font=北師大說文小篆&size=100&style=regular&color=%23000000"
    #         #url2 = url.encode('utf8')
    #         #print(url)
    #         urllib.request.urlretrieve(url, "./chars/"+c[1]+".png")
    #         print(count)
    #         count+= 1

    def get_image2(self):
        #self.browser.find_element_by_xpath('//*[@id="BasicFrom"]/table[1]/tbody/tr[8]/td[2]/a').click()
        #sleep(2)
        #self.browser.find_element_by_xpath('//*[@id="KaishuFreqCheck"]').click()
        #elem = self.browser.find_element_by_xpath('//*[@id="KaishuFreqOrder"]')
        #elem.click()
        #elem.clear()
        #elem.send_keys("100000") #frequency is set at 10000
        #self.browser.find_element_by_xpath('//*[@id="OptionsAccept"]').click()
        self.browser.find_element_by_xpath('//*[@id="Submit"]').click()
        sleep(10) # change pic load to false!!
        page_info = self.browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/form/table[1]/tbody/tr/td').text
        page_info = page_info.split('／')[1].split('頁')[0]
        print("total pages: ", page_info)
        ch_orders = []
        for i in range(int(page_info)):
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
                    #    print("cant")
                    kai_order = query.get_attribute("href").split('=')[-1]
                    ch_order = query.text
                    if ch_order in ch_orders:
                        continue
                    ch_orders.append(ch_order)
                    
                    
                    img_url = self.browser.find_element_by_xpath('//*[@id="HiddenFrom"]/div/table/tbody/tr['+str(tr_)+']/td['+str(td_)+']/img').get_attribute("src")
                    img_url_ls = img_url.split("size=")
                    img_url_ls[1] = "size=400" + img_url_ls[1][2:]
                    img_url = ''.join(img_url_ls)
                    print(img_url)
                    urllib.request.urlretrieve(img_url, "./db/img/"+kai_order+".png")
                    print(ch_order)
            if (i + 1 != int(page_info)):
                self.browser.find_element_by_xpath('//*[@id="PageLink' + str(i + 2) + '"]').click()

    def get_freq(self):
        with open('./db/freq.json', 'r') as f:
            freq_max = json.load(f)
        value_list = list(freq_max.values())
        n_queries = len(set(value_list))
        print(n_queries)
        added = max(value_list)
        self.freq = added
        if (self.freq) >= 3000 :
            return
        
        sleep(10) # set dont show image on browser by human!!
        for freq_now in range(40*n_queries,10000,40):
            self.browser.find_element_by_xpath('//*[@id="BasicFrom"]/table[1]/tbody/tr[8]/td[2]/a').click()
            sleep(1)
            if not self.enabled:
                self.browser.find_element_by_xpath('//*[@id="KaishuFreqCheck"]').click()
            self.enabled = True
            elem = self.browser.find_element_by_xpath('//*[@id="KaishuFreqOrder"]')
            elem.click()
            elem.clear()
            elem.send_keys(str(freq_now))
            self.browser.find_element_by_xpath('//*[@id="OptionsAccept"]').click()
            enabled = True
            self.browser.find_element_by_xpath('//*[@id="Submit"]').click()
            sleep(2)
            page_info = self.browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/form/table[1]/tbody/tr/td').text
            page_info = page_info.split('／')[1].split('頁')[0]
            print("freq barrier: ",freq_now," total pages: ", page_info)
            ch_orders = []

            for i in range(int(page_info)):
                sleep(0.5)
                for tr_ in range(1, 11, 2):
                    for td_ in range(1, 21, 2):
                        #xpath = '[@id="HiddenFrom"]/div/table/tbody/tr[' + str(tr_) + ']/td[' + str(td_) + ']/a'
                        xpath2 = '/html/body/table[2]/tbody/tr/td[3]/form/div/table/tbody/tr[' + str(tr_) + ']/td[' + str(td_) + ']/a'
                        #'/html/body/table[2]/tbody/tr/td[3]/form/div/table/tbody/tr[1]/td[3]/a'
                        try:
                            query = self.browser.find_element_by_xpath(xpath2)
                        except:
                            sleep(2)
                            try:
                                query = self.browser.find_element_by_xpath(xpath2)
                            except:
                                print("can't find! likely end of query")
                                break
                        while(True):
                            try:
                                ch_order = query.text
                                kai_order = query.get_attribute("href").split('=')[-1]
                            except(StaleElementReferenceException):
                                return #reparse
                                
                            except:
                                break
                            else:
                                break
                        
                        #    print("cant")
                        if ch_order in ch_orders:
                            continue
                        
                        if kai_order in freq_max:
                            continue
                        freq_max[kai_order] = 0
                        added += 1
                if (i + 1 != int(page_info)):
                    try:
                        self.browser.find_element_by_xpath('//*[@id="PageLink' + str(i + 2) + '"]').click()
                    except(WebDriverException):
                        sleep(2)
                        try:
                            self.browser.find_element_by_xpath('//*[@id="PageLink' + str(i + 2) + '"]').click()
                        except:
                            i-=1
                        
            for k in freq_max:
                if freq_max[k] == 0:
                    freq_max[k] = added
            print("finish parsing zhuan to: ", added)
            with open('freq.json', 'w') as f:
                json.dump(freq_max, f)
        

        
c = Crawler()
#for i in range(1, 100):
#    c.q_draw(i)
# with open("database.txt", "r",encoding = "utf-8") as f:
#     char_idx =   [x.split(',')[0] for x in f.readlines()[1:]]
# url_base = "http://xiaoxue.iis.sinica.edu.tw/xiaozhuan?kaiOrder="
# with open("database_meaning.txt", "r",encoding = "utf-8") as f:
#     done_idx = [line.split('\t')[0] for line in f.readlines()]
#     for d in done_idx:
#         char_idx.remove(d)

#c.get_info(char_idx)
kai_char = []
# with open("database_meaning.txt", "r",encoding = "utf-8") as f:
#     for x in f.readlines():
#         x_s = x.split('\t')
#         if len(x_s[1]) >= 2:
#             print(x_s[1])
#             if not os.path.exists("./chars/" + x_s[0] +".png"):
#                 kai_char.append((x_s[1].split('：')[1][1],x_s[0]))
# kai_char_s = set(kai_char)
# print(len(kai_char_s))
# c.get_image2()
while(True):
    c.get_freq()
    if (c.freq > 3000):
        break


