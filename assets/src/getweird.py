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


    def get_weird(self,weird):
        weird_to_zhuanfontid = {}
        for w in weird:
            try:
                self.browser.find_element_by_xpath('//*[@id="KaishuChar"]').send_keys(str(w))
            except WebDriverException:
                print("can't search",w)
                continue
            self.browser.find_element_by_xpath('//*[@id="Submit"]').click()
            sleep(2)
            try:
                zhuanfontid = self.browser.find_element_by_xpath('//*[@id="HiddenFrom"]/div/table/tbody/tr/td[1]').alt[1:-1]
            except:
                print("can't find",w)
                continue
            weird_to_zhuanfontid[w] = zhuanfontid
            self.browser.find_element_by_xpath('//*[@id="Reset"]').click()
            with open("../db/weird.json","w") as f:
                json.dump(weird_to_zhuanfontid,f)

with open("../db/weird.pkl","rb") as f:
    weird = pkl.load(f)
print(weird)
c = Crawler()
c.get_weird(weird)