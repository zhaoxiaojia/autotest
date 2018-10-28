#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/10/27 8:12
#@Author  :Coco
#@FileName: loginTest.py

#@Software: PyCharm
import unittest
import HTMLTestRunner
import time

class loginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()