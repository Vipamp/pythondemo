# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/10/9 11:37
   @File Name：Demo07.py
   @Python Version: 3.6 by Anaconda
   @Description：一个图上绘制多条曲线，设置图例和位置
'''
import matplotlib.pyplot as plt

#   设置图的名称
plt.title("hello ")

# 设置横纵坐标名称
#   1、折线图
x1 = [1, 2, 3, 4, 5]
y1 = [3, 4, 6, 7, 8]

x2 = [1, 2, 3, 5, 7]
y2 = [1, 4, 8, 6, 7]

plt.plot(x1, y1, 'r', label='redline')  # 绘制x1,y1的直线
plt.plot(x2, y2, 'b', label='blueline')  # 绘制x2,y2的直线

plt.legend(loc='upper right', frameon=False)  # 显示图例：loc：显示位置framenon：图例是否加边框

plt.show()
