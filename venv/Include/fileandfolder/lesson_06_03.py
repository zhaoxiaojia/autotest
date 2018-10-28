#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2018/10/25 21:27
# @Author  :Coco
# @FileName: lesson_06_03.py

# @Software: PyCharm

import json
import xml.dom.minidom

test1 = {"android": "appium", "web": "selenmium", "interface": u'接口'}
# js = json.dumps(test1, sort_keys=False, indent=4, separators=(',', ':'), encoding='gbk', ensure_ascii=False)
#   把python对象转换成json对象的一个过程
js = json.dumps(test1)
print js
print type(js)
#   讲json对象转换成python对象
j_python = json.loads(js)
print j_python
print type(j_python)

#   读json文件
f = open('test.json', 'r')
t = json.load(f)
print t
print type(t)

#   写json文件
f = open("ttt.json", "w")
json.dump(js, f)

dom = xml.dom.minidom.parse('user.xml')
root = dom.documentElement
list = root.getElementsByTagName('user')
print list[1].getAttribute("id")
print list[0].getElementsByTagName('username')[0].childNodes[0].nodeValue

print "for ... "

for i in list:
    print i.getAttribute("id")
    print i.getElementsByTagName("username")[0].childNodes[0].nodeValue
    print i.getElementsByTagName("password")[0].childNodes[0].nodeValue


