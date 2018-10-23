# _*_ coding:utf-8 _*_
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')



#   获取id = kw 元素的name属性
# print(driver.find_element_by_id('kw').get_attribute('name'))
#   获取link_text ’新闻'的text属性
# print(driver.find_element_by_link_text('新闻').get_attribute('text'))


# driver.find_element_by_id('kw').send_keys('pronclub')
#   获取id = kw 元素的value 属性
# print driver.find_element_by_id('kw').get_attribute('value')

#   获取class_name = toindex 元素的text属性
# print driver.find_element_by_class_name('toindex').text

#   通过ActionChains 类的move_to_element 方法模拟鼠标悬停
ActionChains(driver).move_to_element(driver.find_element_by_link_text('设置')).perform()
#   点击设置菜单的子菜单中的选项搜索设置（class_name = setpref）
driver.find_element_by_class_name('setpref').click()

#   点击搜索设置页面中下拉框
# driver.find_element_by_css_selector('#nr > option:nth-child(2)').click()

#   Select 类的使用示例
#   获取id = nr的下拉框元素
se = driver.find_element_by_id('nr')
#   通过下标选择下拉框子选项
# Select(se).select_by_index(2)
#   通过value选择下拉框子选项
# Select(se).select_by_value('20')
#   通过text选择下拉框子选项
# Select(se).select_by_visible_text('每页显示50条')

for i in  range(len(Select(se).options)):
    Select(se).select_by_index(i)
    time.sleep(2)

