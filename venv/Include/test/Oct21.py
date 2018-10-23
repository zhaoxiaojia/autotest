#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2018/10/21 11:12
# @Author  :Coco
# @FileName: lesson_05.py

# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

#   设置google chrome 不提示弹窗通知
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

#   打开新浪邮箱
driver.get('https://mail.sina.com.cn/?from=mail')

#   填写用户名 密码
driver.find_element_by_id('freename').send_keys("geminilichao@sina.cn")
driver.find_element_by_id('freepassword').send_keys('lichao1994')

#   提交
driver.find_element_by_class_name('loginBtn').click()
time.sleep(5)

#   点击写信a
driver.find_element_by_partial_link_text('写信').click()


#   填写主题
driver.find_element_by_xpath('//*[@id="panel_left"]/form/div/table/tbody/tr[6]/td/input').click()
