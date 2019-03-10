# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/10/9 11:42
   @File Name：Demo11.py
   @Python Version: 3.6 by Anaconda
   @Description：3D图形绘制
'''

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
Z = X ** 2 + Y ** 2
plt.xlabel('x coordinate')
plt.ylabel('y coordinate')

plt.title('z=x^2+y^2')
# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1)
ax.scatter(X, Y, Z, color='r')

# plt.savefig('3dpicture.jpg', dpi=200)

plt.show()
