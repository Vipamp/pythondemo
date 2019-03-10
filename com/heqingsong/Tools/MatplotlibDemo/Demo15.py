# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/10/9 11:49
   @File Name：Demo15.py
   @Python Version: 3.6 by Anaconda
   @Description：绘制饼图
'''

import matplotlib.pyplot as plt

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,  # 饼图数据，这里传递的是真实值，显示是按照比例显示
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),  # 指定需要单独拖出来的部分
        autopct='%1.1f%%')  # 显示百分比形式
plt.show()
