# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/10/9 11:22
   @File Name：Demo03.py
   @Python Version: 3.6 by Anaconda
   @Description：使用plot绘制散点图，并指定颜色
'''
import matplotlib.pyplot as plt

#   设置图的名称
plt.title("hello ")

#   1、画散点图
x = [1, 2, 3, 4, 5]
y = [3, 4, 6, 7, 8]
plt.plot(x, y, 'ob')  # 加上参数‘o’，表示画散点图，o后面可以加上颜色，r：red；b：blue等等
plt.show()
