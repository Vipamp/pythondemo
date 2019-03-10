# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:48
   @File Name：Demo02.py
   @Python Version: 3.6 by Anaconda
   @Description：文件属性读取
'''

# 1、创建一个文件对象
f = open('test.txt', mode='w+')

# 文件属性
print("文件test.txt是否关闭：", f.closed)
print("文件test.txt的访问模式：", f.mode)
print("文件test.txt的名称为：", f.name)
