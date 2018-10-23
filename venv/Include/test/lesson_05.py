#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2018/10/21 11:12
# @Author  :Coco
# @FileName: lesson_05.py

# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

#   设置google chrome 不提示弹窗通知
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

#   打开新浪邮箱
driver.get('https://mail.qq.com/')

#   填写用户名 密码
driver.switch_to.frame('login_frame')
driver.find_element_by_id('u').send_keys("799833928@qq.com")
driver.find_element_by_id('p').send_keys('lichao1994')

#   提交
driver.find_element_by_id('login_button').click()
time.sleep(5)

#   点击写信
driver.find_element_by_id('composebtn').click()


#   填写主题
driver.switch_to.frame('mainFrame')
driver.find_element_by_id('subject').send_keys(u"午夜激情x在线观看")
#   添加附件-方法1
# driver.find_element_by_name('UploadFile').send_keys(r'C:\Users\gemin\Desktop\UsbEAm Hosts Editor\gzip.dll')
#   添加附件-方法2
# driver.find_element_by_id('AttachFrame').click()
# os.system('qq_attach.exe')
#   切换回默认
driver.switch_to.default_content()
#   收信按钮
driver.find_element_by_id('readmailbtn_link').click()
time.sleep(1)
driver.find_element_by_css_selector('#composeExitAlert_QMDialog_btn_delete_save').click()
