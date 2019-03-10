# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/10/9 11:41
   @File Name：Demo10.py
   @Python Version: 3.6 by Anaconda
   @Description：多曲线绘制
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 6, 0.1)

plt.plot(x, [xi ** 2 for xi in x], label='First', linewidth=4, color=(0, 0, 0))
plt.plot(x, [xi ** 2 + 2 for xi in x], 'g', label='second')
plt.plot(x, [xi ** 2 + 5 for xi in x], color=(1, 0, 1, 1), label='Third')
plt.plot(x, [xi ** 2 + 9 for xi in x], color='#BCD2EE', label='Fourth')
plt.axis([0, 7, -1, 50])
plt.xticks(np.arange(0.0, 6.0, 2.5))
plt.xlabel("x", fontsize=15)
plt.ylabel(r'y')
plt.title('simple plot')
plt.legend(loc=1)  # 改变图标位置
plt.grid(True)
# plt.savefig('simple plot.jpg', dpi=200)

# print mpl.rcParams['figure.figsize']       #return 8.0,6.0
#
# print mpl.rcParams['savefig.dpi']          #default to 100              the size of the pic will be 800*600

plt.show()
