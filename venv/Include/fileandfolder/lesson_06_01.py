#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2018/10/25 20:31
# @Author  :Coco
# @FileName: lesson_06_01.py

# @Software: PyCharm

import xlrd
import xlwt
'''
读取excel
xls = xlrd.open_workbook('ex.xlsx')
#   通过下标获取sheet
# sheet = xls.sheets()[0]
#   通过名字获取sheet
# sheet = xls.sheet_by_name('test')
#   通过索引获取sheet
sheet = xls.sheet_by_index(0)
#   获取总行数
print sheet.nrows
#   获取总列数
print sheet.ncols
print sheet.row_values(0)[0]

for i in range(sheet.nrows):
    # print str(i)+u'列'
    # print sheet.row_values(i)[0]
    print sheet.row(i)[0].value

print sheet.cell(0,0).value

for i in range(sheet.ncols):
    print sheet.row_values(0)[i]
'''

ex = xlwt.Workbook()
sheet = ex.add_sheet('test1')
sheet.write(0,0,'coco')
ex.save('t.xls')

