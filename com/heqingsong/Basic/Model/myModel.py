# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/24 16:58
   @File Name：myModel.py
   @Python Version: 3.6 by Anaconda
   @Description：自定义模块
'''


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b != 0:
        return a / b
    else:
        return None
