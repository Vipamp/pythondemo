# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/19 18:42
   @File Name：Condition.py
   @Python Version: 3.6 by Anaconda
   @Description：条件语句
'''
'''
    布尔值：
    False、None，0，""，()，[]，{}都表示False
         其他都为True
        
    条件语句:
    1、if-else;
    2、if-elif-else;（可以多次使用elif）
    3、if语句块内允许嵌套

    注意：
    1、每个条件后面要使用冒号（:），表示接下来是满足条件后要执行的语句块。
    2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
    3、没有switch – case语句。
'''

#    一般的if语句
if 10 == int("10"):
    print("10==int('10')")

#    简单条件语句：if-else
inputNum = int(input("请输入一个数"))
if inputNum == 0:
    print("你输入的数为0")
else:
    print("你输入的数不是0")

#    复杂条件语句：if-elif-else
inputNum = int(input("\n请输入一个数"))
if inputNum == 0:
    print("你输入的数为0")
elif inputNum > 0:
    print("你输入的数大于0")
else:
    print("你输入的数小于0")

#    嵌套条件语句
num = int(input("\n请输入一个数"))
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字可以整除 2 和 3")
    else:
        print("你输入的数字可以整除 2，但不能整除 3")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除 3，但不能整除 2")
    else:
        print("你输入的数字不能整除 2 和 3")
