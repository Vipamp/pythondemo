# -*- coding: utf-8 -*-
'''
Created on 2017年12月15日下午5:03:18
@author: HeQingsong
'''

#    List类型，使用[]，类似于C语言的数组
 
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2, True, 1 - 2j]
tinylist = [123, 'runoob']
 
print (list)  # 输出完整列表
print (list[0])  # 输出列表第一个元素
print (list[1:3])  # 从第二个开始输出到第三个元素
print (list[2:])  # 输出从第三个元素开始的所有元素
print (tinylist * 2)  # 输出两次列表
print (list + tinylist)  # 连接列表

# List中的指定索引的值可以改变
list[0] = "你好"  # 只替换一个索引
list[1:2] = ['我是1', 2]  # 多索引替换
list[4:] = [1]  # 向最后位替换
print(list)
list[1:2] = []  # 删除元素，删除就是将指定的内容替换为空
print(list) 

