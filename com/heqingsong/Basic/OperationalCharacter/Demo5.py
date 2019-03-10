# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/24 17:22
   @File Name：Demo5.py
   @Python Version: 3.6 by Anaconda
   @Description：逻辑运算符
'''

'''
    逻辑运算符：
    and    x and y 
    or    x or y   
    not    not x   
    
    备注：
    1、没有  && ，有 and 代替  ：    flag1 && flag2    ====>    flag1 and flag2
    2、没有|| ，有 or 代替       ：   flag1 || flag2    ====>    flag1 or flag2
    3、没有!， 有not代替            ：    !flag             ====>    not flag
'''

#    变量0可以表示False，其他都为True
a = 10
b = 20

if (a and b):
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

# 修改变量 a 的值
a = 0
if (a and b):
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")

if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")

if (not a or not b):
    print("dfs")
