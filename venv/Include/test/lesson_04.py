#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2018/10/21 10:03
# @Author  :Coco
# @FileName: lesson_04.py

# @Software: PyCharm


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys('pronclub')
time.sleep(1)
#   提供某元素
# driver.find_element_by_id('su').submit()
print driver.current_window_handle
print driver.current_url
#   获取某元素信息
# print driver.find_element_by_id('kw').is_selected()
# print driver.find_element_by_id('kw').is_enabled()
# print driver.find_element_by_id('kw').is_displayed()
#   清空指定元素
# driver.find_element_by_id('kw').clear()
#   退出浏览器
# driver.quit()
