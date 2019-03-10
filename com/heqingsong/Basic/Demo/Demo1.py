# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/24 20:27
   @File Name：Demo1.py
   @Python Version: 3.6 by Anaconda
   @Description：//TODO
'''

#    列举所有的关键字
#    '''多行注释，使用#作为单行注释
import keyword
from builtins import int
print(keyword.kwlist)

#    缩进格式，使用空格缩进，表示一个代码块，但是同一个代码块的语句必须包含相同的缩进空格数
if True:
    print("true")
else: 
    print('false')

#    数据类型只有四种：
#    整数：1
#    长整数：比较大的整数
#    浮点数：如1.23    3E-2
#    复数：如 1+2j
i = 1 + 2j
print(i)

#    单引号和多引号都可以表示字符串
s = "this " "is " "string";  #    字符串可以直接接连
print(s)

# in1 = input("请输入一个加数:")
# in2 = input("请输入一个加数:")
# print("你输入的值是:" + (in1 + in2));

#    如果在同一行写多条语句，使用冒号分割
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

#    print默认输出是换行的，如果不换行，需要加上end=" "
print("这句话不换行", end="（不换行结尾 ）            ")
print("换行")

