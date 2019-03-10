# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/10/9 11:38
   @File Name：Demo08.py
   @Python Version: 3.6 by Anaconda
   @Description：简单绘图的综合案例
'''

import matplotlib.pyplot as plt


# 折线图
def linePlots():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

    plt.plot(x, y)
    plt.show()


# 散点图
def scatterPlots():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

    #   plt.plot(x, y, 'o')  # 加一个参数'o'就是散点图了
    plt.scatter(x, y)
    plt.show()


# 散点图设置颜色
def colorScatterPlots():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

    plt.plot(x, y, 'or')  # 加一个参数'r'就可以变换颜色了
    plt.show()


# 其中：r:red,b:blue,g:green,y:yellow,k:black,w:white,c:cyan蓝绿色,m:magenta品红
# 设置线条样式
def styleLinePlots():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

    plt.plot(x, y, '--')  # 可以设置线条样式
    plt.show()


# 其中有：--，-，-.，：,None
# 设置标记点的样式
def styleScatterPlots():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

    plt.plot(x, y, 'dr')  # 设置散点形式，并且同时设置颜色
    # 实测改变两个字母的顺序不影响
    plt.show()


# *：五角星，s:方块，p:五边形，h:六边形，H：六边形，还有：+ x D d（菱形）
# 设置图表标题，坐标轴标题，坐标轴的最大范围
def titleOlimitsPlots():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

    plt.plot(x, y)

    plt.title('mytitle')  # 设置图表标题
    plt.xlabel('x axis')  # 设置X坐标轴标题
    plt.ylabel('y axis')  # 设置Y坐标轴表
    plt.xlim(0.0, 7.0)  # 设置坐标轴的范围
    plt.ylim(0.0, 30.0)

    plt.show()


# 设置一下坐标轴的间隔及显示的内容
def ticksPlots():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

    plt.plot(x, y)

    plt.title('mytitle')  # 设置图表标题
    plt.xlabel('x axis')  # 设置X坐标轴标题
    plt.ylabel('y axis')  # 设置Y坐标轴表
    plt.xlim(0.0, 7.0)  # 设置坐标轴的范围
    plt.ylim(0.0, 30.0)

    plt.xticks([2, 4])  # 设置x轴的标签间隔
    plt.yticks([4, 16])  # 设置y轴的标签间隔

    plt.show()


# 一个坐标轴上画多条线或者图
def manyPlots():
    x1 = [1, 2, 3, 4, 5]
    y1 = [1, 4, 9, 16, 25]

    x2 = [1, 2, 4, 6, 8]
    y2 = [2, 4, 8, 12, 16]

    plt.plot(x1, y1, 'r')
    plt.plot(x2, y2, 'g')

    plt.title('mytitle')  # 设置图表标题
    plt.xlabel('x axis')  # 设置X坐标轴标题
    plt.ylabel('y axis')  # 设置Y坐标轴表
    plt.xlim(0.0, 9.0)  # 设置坐标轴的范围
    plt.ylim(0.0, 30.0)

    plt.show()


# 图例 Figure legends ,即标识
def legendsPlots():
    x1 = [1, 2, 3, 4, 5]
    y1 = [1, 4, 9, 16, 25]

    x2 = [1, 2, 4, 6, 8]
    y2 = [2, 4, 8, 12, 16]

    plt.plot(x1, y1, 'r', label='redline')  # 设置好图例要显示的内容
    plt.plot(x2, y2, 'g', label='greenline')  #

    plt.title('mytitle')  # 设置图表标题
    plt.xlabel('x axis')  # 设置X坐标轴标题
    plt.ylabel('y axis')  # 设置Y坐标轴表
    plt.xlim(0.0, 9.0)  # 设置坐标轴的范围
    plt.ylim(0.0, 30.0)

    plt.legend(loc='upper right', frameon=True)
    # 设置图例
    # 位置:‘upper right’, ‘upper left’, ‘center’, ‘lower left’, ‘lower right’
    # frameon：图例上的那个框

    plt.show()


legendsPlots()
