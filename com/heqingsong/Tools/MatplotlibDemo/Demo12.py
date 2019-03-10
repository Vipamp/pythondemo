# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/10/9 11:46
   @File Name：Demo12.py
   @Python Version: 3.6 by Anaconda
   @Description：绘制条形图
'''

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [4, 2, 5, 6, 8, 4, 3, 2]

plt.bar(x, y)
plt.show()

# 2、条形图的横坐标可以不连续
x = [1, 2, 3, 5, 6, 8]
y = [4, 2, 5, 6, 8, 2]

plt.bar(x, y, label='Pic1')
plt.bar([4, 7], [4, 1], label='Pic2')
plt.show()
