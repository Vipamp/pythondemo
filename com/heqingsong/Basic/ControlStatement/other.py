# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/19 18:56
   @File Name：other.py
   @Python Version: 3.6 by Anaconda
   @Description：
        几种特殊件语句：
            （1）exec(str)：将字符串当成代码执行
'''

'''
    其他几个特殊的代码：
'''

# exec，执行动态代码，即把字符串当成python语句执行
strIn = input("请输入你要执行的语句，例如：print('Hello Wolrd!')\n")
exec(strIn)

# eval：计算字符串算式
strIn = input("请输入你要计算的公式，例如：1+2+3+4：\n")
print(eval(strIn))
