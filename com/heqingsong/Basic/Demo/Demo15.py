# -*- coding: utf-8 -*-
'''
Created on 2018年5月23日下午1:27:42
@author: HeQingsong
@description:
        随机生成10位数密码
'''

import random

pwdList = ""
for i in range(0, 62):
    if i < 10:
        pwdList += str(i)
    elif i >= 10 and i < 36:
        pwdList += chr(i - 10 + ord('a'))
    else:
        pwdList += chr(i - 36 + ord('A'))

for i in range(0, 10):
    passwd = ""
    for i in range(0, 8):
        passwd += pwdList[random.randint(0, 61)]
    print(passwd)
