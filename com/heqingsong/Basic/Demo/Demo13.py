# -*- coding: utf-8 -*-
'''
Created on 2018年3月28日下午6:53:43
@author: HeQingsong
@description:
'''

inputNum = int(input("请输入一个5位数："))
if(inputNum // 10000 == inputNum % 10):
    if(inputNum // 1000 % 10 == inputNum // 10 % 10):
        print("这个数是回文数")
    else:
        print("这个数不是回文数")
else:
    print("这个数不是回文数")
