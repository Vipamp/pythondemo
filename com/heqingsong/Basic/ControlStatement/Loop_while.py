# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/19 18:51
   @File Name：Loop_while.py
   @Python Version: 3.6 by Anaconda
   @Description：while循环语句
'''

'''
    while循环；（Python没有do{}while循环）
            （1）while：
            （2）while-else：(不管while条件一开始就不满足还是执行后不满足，else语句都会执行一次，如果循环时使用break退出循环，不执行else)
                备注：如果循环体只有一条语句，可以直接在冒号后写，和while写在同一行
    
    while循环体中可以使用break，效果和java一致，如果使用break跳出循环体，else语句的内容也不会执行
'''

#    while循环：
inputNum = int(input("请输入一个数n："))
i = 0
sum = 0
while inputNum >= i:
    sum += i
    i += 1
print("1+2+3+…+n的结果是%d" % (sum))

#    while-else循环：
inputNum = int(input("请输入一个数n："))
i = 0
sum = 0
while inputNum >= i:
    sum += i
    i += 1
else:
    print("执行完毕")
print("1+2+3+…+n的结果是%d" % (sum))
