'''
   @Author：HeQingsong
   @Date：2018/10/9 11:54
   @File Name：
   @Python Version: 3.6 by Anaconda
   @Description：绘制动画
'''
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# 1、新建一个Figure
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)


# 2、初始化
def init():
    line.set_data([], [])
    return line,


# 3、编写动画函数，i是帧编号
def update(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x + 0.01 * i))  # 调整x相当于向右平移图像
    line.set_data(x, y)
    return line,


# 4、绘制动画
# 画布， 使用帧数做参数的绘制函数， init生成器
# frames=200   帧数
# interval=20  间隔
anim = animation.FuncAnimation(fig, update, init_func=init, frames=200, interval=20, blit=False)

plt.show()
