from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
import json
import pickle as pkl
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
        self.browser = webdriver.Chrome(self.driver)
        self.mouse = webdriver.common.action_chains.ActionChains(self.browser)
        # self.browser.get('https://content.steeluniversity.org/simulators/bos/index.html')
        self.browser.get('http://xiaoxue.iis.sinica.edu.tw/ccdb?ccmapcode=4')
        print('web reached')

        self.font_ids = []

    def get_freq(self,f):
        
        sleep(10) # set dont show image on browser by human!!
        self.browser.find_element_by_xpath('//*[@id="BasicFrom"]/table[1]/tbody/tr[8]/td[2]/a').click()
        sleep(1)
        self.browser.find_element_by_xpath('//*[@id="KaishuFreqCheck"]').click()
        self.enabled = True
        elem = self.browser.find_element_by_xpath('//*[@id="KaishuFreqOrder"]')
        elem.click()
        elem.clear()
        elem.send_keys(str(f))
        self.browser.find_element_by_xpath('//*[@id="OptionsAccept"]').click()
        enabled = True
        self.browser.find_element_by_xpath('//*[@id="Submit"]').click()
        sleep(2)
        page_info = self.browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/form/table[1]/tbody/tr/td').text
        page_info = page_info.split('／')[1].split('頁')[0]

        print("total pages: ", page_info)
        ch_orders = []

        for i in range(int(page_info)):
            sleep(2)
            all_fonts = self.browser.find_elements_by_class_name('charValue')
            self.font_ids += [x.get_attribute("alt") for x in all_fonts]
            if (i + 1 != int(page_info)):
                try:
                    self.browser.find_element_by_xpath('//*[@id="PageLink' + str(i + 2) + '"]').click()
                except(WebDriverException):
                    sleep(2)
                    try:
                        self.browser.find_element_by_xpath('//*[@id="PageLink' + str(i + 2) + '"]').click()
                    except:
                        i-=1
        print("finish parsing zhuan to: ", f)
        with open('../db/freq3000.pkl', 'wb') as f:
            pkl.dump(c.font_ids, f)
        

freq = 3000  
c = Crawler()
c.get_freq(freq)
print("finish getting zhuan words under freq",freq)

