# -*- coding: utf-8 -*-
'''
Created on 2017年12月15日下午5:03:18
@author: HeQingsong
'''

#    Tuple原组（和List类似）
#    List使用[]定义元素，Tuple使用()定义，都是用，分开，可以存放不同的数据类型
#    取数都是使用[]取数
#    List的元素可以通过索引位修改，Tuple的元素不能修改

#    string、list和tuple都属于sequence（序列）。

tuple = ('abcd', 786 , 2.23, 'runoob', 70.2)
tuple2 = (123,)  # 如果只有一个元素，需要加上逗号
 
print (tuple)  # 输出完整列表
print (tuple[0])  # 输出列表第一个元素
print (tuple[1:3])  # 从第二个开始输出到第三个元素
print (tuple[2:])  # 输出从第三个元素开始的所有元素
print (tuple * 2)  # 输出两次列表
print (tuple + tuple2)  # 连接列表
