#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2018/10/22 6:42
# @Author  :Coco
# @FileName: lesson_07.py

# @Software: PyCharm

from pywinauto.application import Application
import time

app = Application()
app = app.connect(title_re=u'打开', class_name='#32770')
app[u'打开']['Edit1'].set_edit_text('C:\Users\gemin\Desktop\UsbEAm Hosts Editor\gzip.dll')
time.sleep(2)
app[u'打开']['Button1'].click()
