# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:57
   @File Name：Demo4.py
   @Python Version: 3.6 by Anaconda
   @Description：函数参数列表，默认值，和可变长参数
'''

'''
    函数传递参数技巧
'''


#    可以直接在调用函数时给参数赋值，此时形参和实参按照参数名对应，而不是按照参数列表对应
def printinfo(name, age):
    print("\n名字: ", name)
    print("年龄: ", age)


printinfo(age=50, name="runoob")
printinfo(name="runoob", age=50)


#    可以使用默认参数，age使用=号赋默认值，可以传，也可以不传，如果传，age按照传递的参数算，如果不传，按照默认值。
#    通常，将必须要传递的参数放前面，带默认参数的放后面
def printInfo2(name, age=50):
    print("\n名字: ", name)
    print("年龄: ", age)


printInfo2("Hqs", 30)
printInfo2("Hqs")


#    可变长参数，可变长参数使用*表示，传入的实际是将参数转换为元组的形式，不是列表，参数在调用方法中不可改变
def printInfo3(*varTuple):
    #    varTuple[0]=2;    #这里报错，varTuple是元组，不可以修改。
    for x in varTuple:
        print(x, end=",")


printInfo3(10, 20, 30)
