# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:49
   @File Name：Demo0.py
   @Python Version: 3.6 by Anaconda
   @Description：序列的装包余与解包，这个实现了一个方法，可以返回多个参数
'''

# 1、装包
value = 1, 2, 3
print(value)

# 2、解包
x, y, z = value
print(x)

# 3、转换为list
li = list(value)
print(li)

# 3、转换为tuple
tu = tuple(value)
print(tu)
