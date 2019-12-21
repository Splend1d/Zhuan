# -*- coding: UTF-8 -*-
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

        self.majors = set()
        self.majors_error = []

        self.browser.get('http://xiaoxue.iis.sinica.edu.tw/ccdb?ccmapcode=4')
        print('web reached')
        sleep(15)#set view image to false 


    def get_basic(self):
        all_info = {}
        self.browser.get("http://xiaoxue.iis.sinica.edu.tw/xiaozhuan")
        for idx in range(1,9832):
            self.browser.find_element_by_xpath('//*[@id="ZiOrder"]').send_keys(str(idx))
            self.browser.find_element_by_xpath('//*[@id="Submit"]').click()
            while(True):
                try:
                    n_results = self.browser.find_element_by_xpath('//*[@id="HiddenFrom"]/table/tbody/tr[2]/td').text
                    
                except:
                    sleep(0.01)
                else:
                    break
            origin = self.browser.find_element_by_xpath('//*[@id="HiddenFrom"]/table/tbody/tr[4]/td[1]').text
            try:
                self.majors.add(d["origin"].split('‧')[1][0])
            except:
                pass
            meaning = self.browser.find_element_by_xpath('//*[@id="PageResult"]/dl/dd[1]').text
            all_fonts = self.browser.find_elements_by_class_name('charValue')
            font_ids = [x.get_attribute("alt") for x in all_fonts]
            all_info[idx] = {"meaning":meaning,"origin":origin,"fonts":font_ids}
            with open("../db/main.pkl", "wb") as f:
                pkl.dump(all_info,f)
            with open("../db/majors.pkl", "wb") as f:
                pkl.dump(self.majors,f)
            self.browser.find_element_by_xpath('//*[@id="Reset"]').click()
            
    def get_major_coverage(self):
        self.browser.get('http://xiaoxue.iis.sinica.edu.tw/ccdb?ccmapcode=4')
        count = 0
        cover = {}
        for m in self.majors:
            try:
                self.browser.find_element_by_xpath('//*[@id="XiaozhuanRadical"]').send_keys(m)
            except WebDriverException:
                self.majors_error.append(m)
                continue
            self.browser.find_element_by_xpath('//*[@id="Submit"]').click()
            sleep(2)
            page_info = self.browser.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[3]/form/table[1]/tbody/tr/td').text
            n_pages = page_info.split('／')[1].split('頁')[0]
            xpath2 = '/html/body/table[2]/tbody/tr/td[3]/form/div/table/tbody/tr[1]/td[1]/a'
            query = self.browser.find_element_by_xpath(xpath2)
            min_zhuan_id = query.text
            try:
                self.browser.find_element_by_xpath('//*[@id="PageLink'+n_pages+'"]').click()
                sleep(2)
            except NoSuchElementException:
                print("only one page")
                if n_pages != "1":
                    print("error",n_pages)
                    s()
            zhuan_ids = [x.text for x in self.browser.find_elements_by_class_name("CharList")]
            while(zhuan_ids[-1].isspace()):
                zhuan_ids.pop()
            max_zhuan_id = zhuan_ids[-1]

            
            print(min_zhuan_id)
            print(max_zhuan_id)
            cover[m] = [min_zhuan_id,max_zhuan_id]
            self.browser.find_element_by_xpath('//*[@id="Reset"]').click()
            count += 1
            print("finished parsing",m,cover[m])
        with open("../db/majors_error.pkl", "wb") as f:
            pkl.dump(self.majors_error,f)
        
        with open("../db/majors_coverage.pkl", "wb") as f:
            pkl.dump(cover,f)
            

    
        
c = Crawler()

# c.get_basic()
# need to get self.majors first!!
with open("../db/majors.pkl", "rb") as f:
    c.majors = pkl.load(f)
c.get_major_coverage()
print("all done")