# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/24 17:06
   @File Name：Demo01.py
   @Python Version: 3.6 by Anaconda
   @Description：测试斐波拉切数列
'''

list = [0, 1]

for x in range(8):
    list.append(list[x] + list[x + 1])

print(list)
print(len(list))


def fib(num=5):
    list = [0, 1]
    for x in range(num):
        list.append(list[x] + list[x + 1])
    return list


print(fib())
print(fib(10))
