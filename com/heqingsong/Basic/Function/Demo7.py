# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 15:08
   @File Name：Demo7.py
   @Python Version: 3.6 by Anaconda
   @Description：函数的可变长参数和固定参数一起使用的情况
'''

'''
    多参数：
        在支持多参数时，使用 *表示是可变参数
       在方法中，可变参数列表结果为一个元组，如果在调用方法时，传递的参数如果不放元组内，需要指定参数名称
'''


# 1、可变参数
def myFun(*arg, name='world'):
    print(arg)
    print(name)
    print(type(arg))


myFun('Hello', 'python', '!', name='sd')
myFun('Hello', 'world', 'my', 'name', 'is', 'HQS')


# 2、可变参数反转
def add(x, y):
    return x + y


param = (1, 2)
print(param)
print(add(*param))
