# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 15:01
   @File Name：Demo6.py
   @Python Version: 3.6 by Anaconda
   @Description：函数的全部变量和局部变量
'''

num = 34


# 如果函数只读取局部变量，可以不使用global修饰，如果需要修改外部变量的值，必须要加上global关键词修饰，否则报错。
# 如果函数里面有个和全局变量重名的变量，没有用global修改，就是局部变量，修改的值不影响全局重名变量的值
def fun1():
    print("\n\nfun1:")
    global num
    print(num)
    num = 123
    print(num)


def fun2():
    print("\n\nfun2:")
    print(num)

def fun3():
    print("\n\nfun3:")
    num = 10
    print(num)
    num = 20
    print(num)

fun1()
fun2()
fun3()
fun2()
