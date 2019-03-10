# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/10/9 11:48
   @File Name：Demo14.py
   @Python Version: 3.6 by Anaconda
   @Description：绘制堆叠图
'''
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

# 指定对叠层的颜色，可有可无
plt.plot([], [], color='m', label='Sleeping', linewidth=2)
plt.plot([], [], color='c', label='Eating', linewidth=2)
plt.plot([], [], color='r', label='Working', linewidth=2)
plt.plot([], [], color='k', label='Playing', linewidth=2)

plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])
plt.legend(loc=2)

plt.xlabel('x')
plt.ylabel('y')
plt.show()
