# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/24 17:08
   @File Name：Demo02.py
   @Python Version: 3.6 by Anaconda
   @Description：递归方式求阶乘
'''


def res(n):
    if n == 0:
        return 1
    else:
        return n * res(n - 1)


print(res(3))
