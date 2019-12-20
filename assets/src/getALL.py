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


    def get_info(self):
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
            with open("../db/database_word.pkl", "wb") as f:
                pkl.dump(all_info,f)
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
            sleep(1)
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
            print(count)
            count += 1
        print(self.majors_error)
        with open("../db/database_coverage.pkl", "wb") as f:
            pkl.dump(cover,f)
            

    
        
c = Crawler()

c.get_info()

c.majors.update(['一', '丨', '又', '丶', '𡿨', '𠃉', '丿', '乀', '𠂆', '亅', '𠃊', '乙', '八', '凵', '丩', '十', '𠂇', '𠘧', '卜', '歹', '刀', '乃', '丂', '𠙴', '入', '冂', '𢎘', '冖', '人', '𠤎', '匕', '儿', '卩', '勹', '厶', '厂', '巜', '仌', '匸', '匚', '二', '力', '几', '五', '七', '九', '丁', '了', '三', '士', '屮', '小', '口', '止', '彳', '廴', '干', '廾', '寸', '幺', '刃', '丌', '工', '于', '亼', '夊', '夂', '久', '才', '乇', '囗', '夕', '宀', '𠔼', '巾', '尸', '彡', '山', '广', '丸', '彑', '犬', '大', '尢', '心', '水', '川', '卂', '手', '女', '亡', '弓', '土', '勺', '阜', '己', '子', '𠫓', '巳', '示', '王', '气', '艸', '牛', '辵', '牙', '卅', '𠬜', '爪', '丮', '支', '殳', '攴', '爻', '予', '肉', '丯', '竹', '曰', '兮', '丹', '井', '木', '之', '帀', '生', '日', '月', '毌', '片', '凶', '𣎳', '冃', '巿', '从', '比', '𡈼', '毛', '尺', '方', '兂', '欠', '旡', '丏', '文', '𠨍', '石', '勿', '冉', '火', '夨', '夭', '亢', '夫', '囟', '雲', '不', '戶', '毋', '氏', '戈', '糸', '斤', '斗', '六', '禸', '巴', '壬', '丑', '午', '玉', '釆', '半', '癶', '正', '疋', '冊', '只', '句', '古', '言', '史', '𦘒', '皮', '用', '目', '𦫳', '玄', '左', '甘', '可', '号', '皿', '去', '食', '矢', '弟', '出', '𣎵', '𥝌', '邑', '旦', '禾', '瓜', '穴', '疒', '网', '白', '北', '丘', '衣', '兄', '皃', '司', '巵', '包', '屵', '長', '豕', '亦', '夲', '夰', '立', '永', '民', '氐', '戉', '甾', '瓦', '它', '田', '且', '矛', '四', '宁', '甲', '丙', '戊', '卯', '未', '申', '吅', '此', '行', '舌', '𧮫', '䇂', '共', '聿', '臣', '殺', '自', '𦣹', '羽', '羊', '冓', '𢆶', '叀', '𠬪', '死', '冎', '㓞', '耒', '箕', '旨', '虍', '血', '青', '倉', '缶', '畐', '舛', '叒', '㫃', '有', '多', '朿', '米', '臼', '尗', '襾', '㐺', '𠂣', '老', '舟', '𠑹', '先', '后', '印', '色', '甶', '屾', '危', '而', '豸', '鹿', '囪', '交', '至', '西', '耳', '曲', '弜', '虫', '劦', '幵', '𠂤', '晶', '辰', '戌', '亥', '上', '告', '走', '步', '㢟', '足', '㕯', '舁', '𦥑', '革', '㼱', '𠦒', '𣦼', '筋', '角', '巫', '豆', '皀', '亯', '𠂹', '束', '貝', '囧', '克', '呂', '㒳', '㡀', '身', '裘', '尾', '禿', '見', '㱃', '㳄', '彣', '㹜', '赤', '谷', '𦣞', '我', '弦', '系', '風', '卵', '里', '男', '車', '辛', '酉', '玨', '隶', '臤', '教', '㸚', '隹', '鳥', '烏', '放', '虎', '京', '㐭', '來', '東', '林', '明', '彔', '𣏟', '帛', '臥', '㣇', '𤉡', '易', '廌', '㲋', '兔', '炎', '炙', '㚔', '亣', '並', '沝', '雨', '非', '門', '金', '叕', '亞', '庚', '是', '品', '音', '𥄎', '眉', '盾', '𥄕', '壴', '會', '高', '𣆪', '韋', '𨛜', '𠧪', '香', '耑', '韭', '重', '頁', '面', '首', '𥄉', '茍', '奢', '思', '泉', '飛', '垚', '厽', '癸', '孨', '酋', '蓐', '犛', '哭', '齒', '丵', '鬲', '鬥', '䀠', '骨', '㠭', '豈', '鬯', '麥', '桀', '𠌶', '員', '倝', '冥', '𣐺', '秝', '宮', '履', '髟', '鬼', '馬', '鼠', '能', '灥', '𠂢', '𠦬', '琴', '素', '絲', '䖵', '蟲', '堇', '畕', '茻', '異', '䰜', '畫', '習', '奞', '巢', '桼', '䢅', '黍', '麻', '瓠', '𦣻', '豚', '魚', '鹵', '率', '黃', '寅', '㗊', '誩', '皕', '雈', '雥', '喜', '舜', '華', '㝱', '黹', '毳', '須', '象', '萈', '黑', '焱', '壺', '壹', '惢', '龜', '黽', '鼓', '豊', '䖒', '嗇', '鼎', '辟', '嵬', '𨺅', '菐', '鼻', '齊', '覞', '麤', '熊', '鱻', '辡', '豐', '稽', '嘼', '龠', '雔', '虤', '𩫏', '㯻', '毇', '燕', '龍', '爨', '羴', '瞿', '鹽', '瀕'])
c.get_major_coverage()