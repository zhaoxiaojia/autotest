# -*-coding:utf-8 -*-
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")


#   通过ID 找到检索框 并往框内输入pronclub字符
# driver.find_element_by_id('kw').send_keys('pronclub')
# driver.find_element_by_id('su').click()

#   通过name 找到检索框，并输入pronclub字符
# driver.find_element_by_name('wd').send_keys('pronclub')

#   通过class_name 找到检索框，并输入pronclub字符
# driver.find_element_by_class_name('s_ipt').send_keys('pronclub')

#   通过link_text 找到'新闻'链接并点击
# driver.find_element_by_link_text('新闻').click()

#   通过partial_link_text 输入部分内容找到'新闻' 链接并点击
# driver.find_element_by_partial_link_text('新').click()

#   通过css_selector 找到检索框并输入pronclub
# driver.find_element_by_css_selector('#kw').send_keys('pronclub')

#   通过xpath 找到检索框并输入pronclub
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('pronclub')

#   通过tag_name 找到form标签并获取其name 属性
# print(driver.find_element_by_tag_name('form').get_attribute('name'))


