#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2018/10/22 19:51
# @Author  :Coco
# @FileName: lesson_03.py

# @Software: PyCharm


import sys

reload(sys)
sys.setdefaultencoding('utf8')

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()

# driver.get("https://passport.ctrip.com/user/login?")
# # driver.get('http://trains.ctrip.com/TrainBooking/SearchTrain.aspx###')
# driver.find_element_by_id('nloginname').send_keys('13023199165')
# driver.find_element_by_id('npwd').send_keys('lichao1994')
# time.sleep(10)
# driver.find_element_by_id('nsubmit').click()
driver.get('http://trains.ctrip.com/TrainBooking/SearchTrain.aspx###')

#   通过JS 去除日期输入框的 readonly 属性
driver.execute_script("document.getElementById('dateObj').value='2018-10-30'")
# driver.find_element_by_id('dateObj').clear()
# driver.find_element_by_id('dateObj').send_keys('2018-12-12')
driver.find_element_by_id('notice01').send_keys(u'杭州')
driver.find_element_by_id('notice08').send_keys(u'上海')

driver.find_element_by_id('searchbtn').click()

time.sleep(3)
strYuding = driver.find_element_by_css_selector('#tbody-01-D93212 > div.railway_list > div.w6 > div:nth-child(1) > a').text
print strYuding
if strYuding == "预订":
    print '已预定'
    # driver.find_element_by_css_selector('#tbody-01-D93212 > div.railway_list > div.w6 > div:nth-child(1) > a').click()
else:
    print "已无票"
# driver.find_element_by_css_selector('#pasglistdiv > div > ul > li:nth-child(2) > input').clear()
# driver.find_element_by_css_selector('#pasglistdiv > div > ul > li:nth-child(2) > input').send_keys(u'李超')
# driver.find_element_by_css_selector('#pasglistdiv > div > ul > li:nth-child(3) > input').clear()
# driver.find_element_by_css_selector('#pasglistdiv > div > ul > li:nth-child(3) > input').send_keys(u'362502199405074417')
# driver.find_element_by_class_name('icon-seat').click()
# driver.find_element_by_css_selector('#contact-mobile').send_keys(r'13023199165')
# driver.find_element_by_css_selector('#btnPay').click()
