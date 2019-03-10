# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/19 18:58
   @File Name：Iteration.py
   @Python Version: 3.6 by Anaconda
   @Description：
        集合的迭代器操作
'''
'''
    迭代器：
        iter(collection)：获取集合的迭代器
        next(iter)：获取迭代器iter的下一个元素的值
    
    可以使用 for i in iter 直接遍历迭代器
'''
list = [1, 2, 3, 4, 5]
it = iter(list)  # 获取list的迭代器对象

#    for循环使用迭代器遍历List
for i in range(5):
    print(next(it))

it = iter(list)
print()
#    for循环直接遍历迭代器
for x in it:
    print(x)
