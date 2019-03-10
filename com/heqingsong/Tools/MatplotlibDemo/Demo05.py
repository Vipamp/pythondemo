# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/10/9 11:27
   @File Name：Demo05.py
   @Python Version: 3.6 by Anaconda
   @Description：绘制散点图，设置散点类型
'''
import matplotlib.pyplot as plt

#   设置图的名称
plt.title("hello ")

#   1、画散点图
x = [1, 2, 3, 4, 5]
y = [3, 4, 6, 7, 8]
plt.plot(x, y, 'r*')
plt.plot(x, [i + 1 for i in y], 'bs')
plt.plot(x, [i + 2 for i in y], 'yh')
plt.plot(x, [i + 3 for i in y], "r+")
plt.show()

'''
    *	五角星
    s	方块
    p	五边形
    h	圆
    H	圆：也是个圆，我没测试出区别
    +	符号本身，不好语言描述
    x	符号本身，不好语言描述
    D	菱形
    d	菱形：只是更长一点
'''
