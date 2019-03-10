# -*- coding: utf-8 -*-
'''
Created on 2018年6月14日下午6:47:25
@author: HeQingsong
@description:
'''

year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

inputYear = int(input("请输入年份"))
inputMonth = int(input("请输入月份"))
inputDay = int(input("请输入日"))

if((inputYear % 4 == 0 and inputYear % 100 != 0) or inputYear % 400 == 0):
    year[1] = 29
sumDay = 0
for i in range(0, inputMonth - 1):
    sumDay += year[i]
sumDay += inputDay

print(sumDay)
