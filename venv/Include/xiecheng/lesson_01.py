#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2018/10/22 7:03
# @Author  :Coco
# @FileName: lesson_01.py

# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://passport.ctrip.com/user/login?")
# driver.get('http://trains.ctrip.com/TrainBooking/SearchTrain.aspx###')
driver.find_element_by_id('nloginname').send_keys('13023199165')
driver.find_element_by_id('npwd').send_keys('lichao1994')
time.sleep(10)
driver.find_element_by_id('nsubmit').click()
driver.get('http://trains.ctrip.com/TrainBooking/SearchTrain.aspx###')

#   通过JS 去除日期输入框的 readonly 属性
driver.execute_script("document.getElementById('dateObj').removeAttribute('readonly')")
driver.find_element_by_id('dateObj').clear()
driver.find_element_by_id('dateObj').send_keys('2018-12-12')
driver.find_element_by_id('notice01').send_keys(u'杭州')
driver.find_element_by_id('notice08').send_keys(u'上海')

driver.find_element_by_css_selector('#searchtype > li.current').click()
