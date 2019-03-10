# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:13
   @File Name：Dictionary4.py
   @Python Version: 3.6 by Anaconda
   @Description：字典的高级2
'''

# 1、clear，清空dict所有值
dict = {'name': 'HQS', 'age': 23}
print(dict)
dict.clear()
print(dict)

# 2、清空关联，直接赋值为{}，和他关联的变量不清空，使用clear()方法，和他相关联的一起清空
print('\n\n')
dict = {'name': 'HQS', 'age': 23}
dict2 = dict
print(dict)
print(dict2)
dict = {}
print(dict2)

print('\n\n')
dict = {'name': 'HQS', 'age': 23}
dict2 = dict
print(dict)
print(dict2)
dict.clear()
print(dict2)
