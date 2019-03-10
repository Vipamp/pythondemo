# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/24 17:23
   @File Name：Demo7.py
   @Python Version: 3.6 by Anaconda
   @Description：身份运算符
'''

'''
    身份运算符：比较两个对象的存储单元
    id(varName)    ：获取变量varName的存储单元
    
    is    is 是判断两个标识符是不是引用自一个对象    x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
    is not    is not 是判断两个标识符是不是引用自不同对象    x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
    
    备注：is 与 == 区别：
    is 用于判断两个变量引用对象是否为同一个：     等同于java的  ==
    == 用于判断引用变量的值是否相等。                    等同于java的  equals
'''

a = 20
b = 20

print("a的地址为：", id(a))
print("b的地址为：", id(b))

if (a is b):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if (id(a) == id(b)):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
print("a的地址为：", id(a))
print("b的地址为：", id(b))

if (a is b):
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if (a is not b):
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")
