# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/10/9 11:17
   @File Name：Demo01.py
   @Python Version: 3.6 by Anaconda
   @Description：测试matplotlib使用plot绘制折线图
'''
import matplotlib.pyplot as plt

#   设置图的名称
plt.title("hello ")

#   1、画折线图
x = [1, 2, 3, 4, 5]
y = [3, 4, 6, 7, 8]
plt.plot(x, y)
# plt.plot(x,y,'r')最后一个参数为线的颜色，r：red；b:blue;g:green等
plt.show()
