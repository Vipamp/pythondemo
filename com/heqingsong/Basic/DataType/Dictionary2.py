# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:08
   @File Name：Dictionary2.py
   @Python Version: 3.6 by Anaconda
   @Description：dictionary类型和其他类型的转换
        list转换成dict
        json转换成dict
'''

# 1、dict函数:将list转换为dict，其中的list必须是二元元组
list = [('name', 'HQS'), ('age', 22)]
dic = dict(list)
print(dic)

# 2、dict构造字典
dic2 = dict(name='HQS', age=23)
print(dic2)

# 3、使用json格式创建字典
json = {'name': 'HQS', 'age': 24}
dic3 = dict(json)
print(dic3)
print(type(dic3))

# 4、查看键值对数量
print('len:', len(dic3))
