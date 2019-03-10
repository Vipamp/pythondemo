# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/10/9 11:39
   @File Name：Demo09.py
   @Python Version: 3.6 by Anaconda
   @Description：结合numpy，常用曲线图的绘制
'''
import numpy as np
from matplotlib import pyplot as plt

#   使用 1 ~ 3*PI，以0.1位步进，生成数组x
x = np.arange(0, 3 * np.pi, 0.1)
print(x)

#   计算sin(x)和cos(x)
siny = np.sin(x)
cosy = np.cos(x)

#   绘图
plt.plot(x, siny, label='sin')
plt.plot(x, cosy, label='cos')
plt.title('sin and cos')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.legend(loc=4)
plt.axis([0, 9, -3, 3])

plt.show()
