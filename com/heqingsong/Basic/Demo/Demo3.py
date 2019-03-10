# -*- coding: utf-8 -*-
'''
Created on 2017年12月15日下午5:03:18
@author: HeQingsong
'''

#    所有变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串
fushu = 1 - 2j  # 复数
fushu2 = 1 + 2j  # 复数
 
print (counter)
print (miles)
print (name)
print(fushu * fushu2)  # 复数可以直接计算

#    多个变量同事赋值
a = b = c = 1
print(a + b + c)

#    多个变量对应赋值
a, b, c = 1, 2, "3"
print(a)
print(b)
print(c)

