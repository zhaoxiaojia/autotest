#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/10/27 7:51
#@Author  :Coco
#@FileName: base.py

#@Software: PyCharm

class base(object):
    def __init__(self,driver):
        self.driver = driver

    def by_id(self,elemeny):
        return self.driver.find_element_by_id(element)

    def by_xpath(self,element):
        return self.driver.find_element_by_xpath(element)

    def by_css(self,element):
        return self.driver.find_element_by_css_selectore(element)


