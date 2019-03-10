# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:34
   @File Name：Demo01.py
   @Python Version: 3.6 by Anaconda
   @Description：try-except异常捕捉
'''
'''
    异常处理；
    1、可以分别捕捉异常，也可以一起捕捉异常
    2、异常后面使用 as加上异常对象
    3、else表示在没有抛出异常时执行
    4、finally语句块可以不写，如果写了，表示不管有没有抛出异常，都会执行

    格式：
    try-except-else-finally，其中的else和finally可以不写
'''
'''
    1、区分异常类型分别捕捉
'''
a = int(input("请输入除数："))
b = int(input("请输入除数："))
try:
    y = a / b
    print(y)
except ZeroDivisionError as e:
    print(e)
    print("除数不能为0")
except TypeError:
    print('数据类型错误')
else:
    print('代码执行正常')
finally:
    print("计算结束")

'''
    2、多异常一起捕捉
'''
try:
    y = a / b
    print(y)
except (ZeroDivisionError, TypeError) as e:
    print("除数不能为0或者数据类型错误")
finally:
    print("计算结束")

'''
    3、全捕捉
'''

try:
    y = a / b
    print(y)
except Exception as e:  # Exception as e可以不写，通常写了，会通过e判断具体的抛出内容
    print("代码执行出现了问题")
finally:
    print("计算结束")
