# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/24 17:11
   @File Name：Demo03.py
   @Python Version: 3.6 by Anaconda
   @Description：二分法查找
'''


def mySearch(list, num):
    i = 0
    l = len(list)
    while (True):
        m = (i + l) // 2
        if (num > list[m]):
            i = m
        elif (num < list[m]):
            l = m
        else:
            return m
        if (i == l - 1):
            return 0 - i - 1


list = [1, 34, 6, 43, 9, 12, 18, 53]
list.sort()

print(list)
print(mySearch(list, 15))
