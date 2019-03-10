# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:50
   @File Name：Demo1.py
   @Python Version: 3.6 by Anaconda
   @Description：函数的基本的定义
'''

'''
    函数：
            函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
            任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
            函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
            函数内容以冒号起始，并且缩进。
     return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
    格式：
    def 函数名（参数列表）:
                函数体（函数体中return可有可无，如果没有，默认返回None）
                
    lambda表达式：
                格式：fun = lambda 参数列表：表达式内容
                例如：fun = lambda x,y:x*y
                        可以把fun当做函数使用，例如：fun(1,2)

    备注：
        （1）函数默认都是有返回值的，如果在定义函数时，没有加上return，则返回None，如果return，按照retrun返回值，调用一个没有返回值的函数，使用变量接收也不会报错。
        （2）方法的备注不是写在方法名上面，是从冒号后一行开始写
'''


def add(a, b):
    #    传基本数据类型为参数
    return a + b


print(add(1, 2))


def area(w, h):
    return w * h


def voidTest():
    print("execute function voidTest")


height = int(input("请输入高度："))
width = int(input("请输入宽："))
print("面积为:", area(width, height))
print("结果为：", voidTest())

# 判断是否可调用，即判断这个变量是否是函数
print(callable(height))  # False
print(callable(area))  # True

# 定义lambda表达式
foo = lambda x, y: x ** y
print(foo(2, 3))
