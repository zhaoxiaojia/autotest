#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2018/10/27 7:56
# @Author  :Coco
# @FileName: loginPage.py

# @Software: PyCharm
import base


class loginPage(base):
    def username(self):
        self.by_id('nloginname').send_keys(u'13023199165')

    def passwd(self):
        self.by_id('npwd').send_keys(u'zhao@123')

    def loginBtn(self):
        self.by_id('nsubmit').click()

    def loginIn(self):
        self.username()
        self.passwd()
        self.loginBtn()