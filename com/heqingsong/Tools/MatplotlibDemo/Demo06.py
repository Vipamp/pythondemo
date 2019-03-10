# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/10/9 11:35
   @File Name：Demo06.py
   @Python Version: 3.6 by Anaconda
   @Description：设置图示的横纵坐标和单位间隔
'''

import matplotlib.pyplot as plt

#   设置图的名称
plt.title("hello ")

# 设置横纵坐标名称
plt.xlabel("x axis")
plt.ylabel("y axis")

# 设置横纵坐标额范围
plt.xlim(0, 5)
plt.ylim(1, 20)

# 设置标签间隔，即指定的坐标值上显示标签，其他的不显示
plt.xticks([2, 4])
plt.yticks([4, 16])

x = [1, 2, 3, 4, 5]
y = [3, 4, 6, 7, 8]
plt.plot(x, y)
plt.show()
