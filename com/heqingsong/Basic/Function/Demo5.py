# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 15:00
   @File Name：Demo5.py
   @Python Version: 3.6 by Anaconda
   @Description：lambda表达式
'''

'''
    lambda表达式：
        lambda [arg1 [,arg2,.....argn]]:expression
                     直接给参数和计算表达式，然后会自动将计算结果当返回值返回
'''
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2


# 等同于：
def sum2(arg1, arg2):
    return arg1 + arg2


# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))
print()
print("相加后的值为 : ", sum2(10, 20))
print("相加后的值为 : ", sum2(20, 20))
