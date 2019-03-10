# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/10/9 11:23
   @File Name：Demo04.py
   @Python Version: 3.6 by Anaconda
   @Description：设置图线类型
'''
import matplotlib.pyplot as plt

#   设置图的名称
plt.title("hello ")

#   1、画散点图
x = [1, 2, 3, 4, 5]
y = [3, 4, 6, 7, 8]
plt.plot(x, y, '-')
plt.plot(x, [i + 1 for i in y], '-.')
plt.plot(x, [i + 2 for i in y], ':')
plt.plot(x, [i + 3 for i in y])
plt.show()

'''
    -:虚线
    -.:点划线
    ::点线
    默认为实线
'''
