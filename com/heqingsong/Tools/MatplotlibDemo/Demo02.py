# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/10/9 11:20
   @File Name：Demo02.py
   @Python Version: 3.6 by Anaconda
   @Description：测试使用scatter绘制散点图
'''
import matplotlib.pyplot as plt

#   设置图的名称
plt.title("hello ")

#   1、画散点图
x = [1, 2, 3, 4, 5]
y = [3, 4, 6, 7, 8]

# 以下的两种方式都可以画散点图，通常使用第二种
# plt.plot(x, y, 'o')  # 加上参数‘o’，表示画散点图
plt.scatter(x, y)
plt.show()
