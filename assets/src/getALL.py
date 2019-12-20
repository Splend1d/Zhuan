import urllib.request
import urllib.parse
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
import json
import random
import pickle as pkl
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
        sleep(15)#set view image to false 


    def get_info(self):
        this_dict = {}
        for idx in range(1,9832):
            self.browser.get("http://xiaoxue.iis.sinica.edu.tw/xiaozhuan")
            self.browser.find_element_by_xpath('//*[@id="ZiOrder"]').send_keys(str(idx))
            self.browser.find_element_by_xpath('//*[@id="Submit"]').click()
            while(True):
                try:
                    n_results = self.browser.find_element_by_xpath('//*[@id="HiddenFrom"]/table/tbody/tr[2]/td').text
                    
                except:
                    sleep(0.01)
                else:
                    break
            meaning = self.browser.find_element_by_xpath('//*[@id="PageResult"]/dl/dd[1]').text
            all_fonts = self.browser.find_elements_by_class_name('charValue')
            font_ids = [x.get_attribute("alt") for x in all_fonts]
            this_dict[idx] = {"meaning":meaning,"fonts":font_ids}
            with open("../db/database_word.pkl", "wb") as f:
                pkl.dump(this_dict,f)
            self.browser.find_element_by_xpath('//*[@id="Reset"]').click()

    
        
c = Crawler()

c.get_info()

