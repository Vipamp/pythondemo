# -*- coding: utf-8 -*-
'''
Created on 2018年5月3日上午11:06:13
@author: HeQingsong
@description:
'''

name1 = input("请输入你的姓名")
name2 = input("请输入恋人姓名")

i1 = hash(name1)
i2 = hash(name2)
i = abs(i1 - i2) % 100

if(i > 90):
    print("很有缘")
elif(i > 80):
    print("有缘")
elif(i > 70):
    print("一般")
elif(i > 60):
    print("无缘")
else:
    print("孽缘")

