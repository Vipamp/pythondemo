'''
   @Author：HeQingsong
   @Date：2018/10/9 11:53
   @File Name：
   @Python Version: 3.6 by Anaconda
   @Description：画布多图绘制和画填充图
   主要方法：
        fill_between(x,y1,y2)
                    可以绘制两条曲线，x-y1，x-y2,然后填充两条曲线中间的部分
'''

import matplotlib.pyplot as plt
import numpy as np

# 1、分割画布，并获取一个子图
ax1 = plt.subplot2grid((1, 2), (0, 0))
ax2 = plt.subplot2grid((1, 2), (0, 1))

# 2、填充子图
x = np.arange(50)
y = [np.sin(i / 5) * 10 for i in x]
ax1.fill_between(x, 0, y, color='y')

# 3、设置网格和坐标轴颜色
ax1.grid(True)
ax1.xaxis.label.set_color('c')
ax1.yaxis.label.set_color('r')

# 3、填充子图
x = np.arange(200)
y1 = [np.sin(i / 5) * 10 for i in x]
y2 = [np.sin(i / 5) * 5 for i in x]
ax2.fill_between(x, y1, y2)  # 绘制填充图：x，y为x、y轴的序列，中间的参数0是平行于x轴的填充分割线

# 4、设置网格和坐标轴颜色
ax2.grid(True)
ax1.xaxis.label.set_color('c')
ax1.yaxis.label.set_color('r')

plt.legend()
plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()
