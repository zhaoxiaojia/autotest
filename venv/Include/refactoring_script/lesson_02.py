#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2018/10/22 21:35
# @Author  :Coco
# @FileName: lesson_02.py

# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import common
driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("http://www.baidu.com")

driver.get("http://trains.ctrip.com/TrainBooking/SearchTrain.aspx###")


def id(element):
    return driver.find_element_by_id(element)


def js(value):
    driver.execute_script("document.getElementById('dateObj').value='%s'" % value)


def css(element):
    return driver.find_element_by_css_selector(element)


js('2018-10-28')
# id('notice01').send_keys(u'上海')
# id('notice08').send_keys(u'北京')
common.id(driver,'notice01').send_keys(u'上海')
common.id(driver,'notice08').send_keys(u'北京')
css('#searchbtn').click()
