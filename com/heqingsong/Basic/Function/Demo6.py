# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 15:01
   @File Name：Demo6.py
   @Python Version: 3.6 by Anaconda
   @Description：函数的全部变量和局部变量
'''

num = 34


# 如果函数只读取外部变量，可以不使用global修饰，如果需要修改外部变量的值，必须要加上global关键词修饰，否则报错。
def fun1():
    print("\n\nfun1:")
    global num
    print(num)
    num = 123
    print(num)


def fun2():
    print("\n\nfun2:")
    print(num)


fun1()
fun2()
