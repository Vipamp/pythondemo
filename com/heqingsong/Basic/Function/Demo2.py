# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:53
   @File Name：Demo2.py
   @Python Version: 3.6 by Anaconda
   @Description：带参数的函数
'''


#    传序列为参数
def sum(list):
    sumNum = 0
    for i in list:
        sumNum += i
    return sumNum


print(sum([1, 2, 3, 4, 5]))


def split(str):
    for i in str:
        print(i, end=" ")


myStr = "Hello World!"
split(myStr)
