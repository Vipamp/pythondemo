# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/24 17:11
   @File Name：Demo04.py
   @Python Version: 3.6 by Anaconda
   @Description：列表推导式作数据筛选
'''
list = [1, 3, 63, 4, 6, 72, 354, 8, 64]

# 筛选出大于10 的数据
list2 = [x for x in list if x > 10]
print("出大于10 的数据：", list2)

# 筛选出可以被4整除的数据
list3 = [x for x in list if x % 4 == 0]
print(list3)
