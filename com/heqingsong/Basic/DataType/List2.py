# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:21
   @File Name：List2.py
   @Python Version: 3.6 by Anaconda
   @Description：list的常用知识
'''

'''
    List函数：
'''

# 1、将字符串拆分成list
str = 'hello'
strList = list(str)
print(strList)

# 2、删除List里面的元素
del strList[2]
print(strList)

# 3、分片赋值
strList[1:] = 'ello'
print(strList)

# 4、向列表里面插入元素
num = [1, 5]
num[1:1] = [2, 3, 4]
print(num)

# 5、从列表中间删除元素
num[1:4] = []
print(num)
