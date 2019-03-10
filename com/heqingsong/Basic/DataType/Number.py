# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:23
   @File Name：Number.py
   @Python Version: 3.6 by Anaconda
   @Description：基本的数字类型及其转换
'''

#    创建变量，并给变量赋值
var1 = 1
var2 = 2

#    销毁变量
del var1, var2

'''
    Number的三种数据类型：int，float，complex（复数）
'''
intNum = 1;
print(intNum)
intNum2 = 0xfe  # 十六进制表示整数，也可以采用八进制
print(intNum)

floatNum = 1.5
print(floatNum)
floatNum2 = 3.24E-2  # 使用科学计数法表示
print(floatNum2)

comNum = 1 + 2j
print(comNum)
comNum2 = complex(1, 3)  # 使用complex赋值，等同于1+3j
print(comNum2)
print(comNum * comNum2)  # 复数可以直接计算

'''
    数据类型转换：
    int(x) 将x转换为一个整数。
    float(x) 将x转换到一个浮点数。
    complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
    complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
    
    注意：
        整数可以转换为浮点数，浮点数不能转换为整数
'''
inputStr = input("请输入一个数字")
InputInt = int(inputStr)
print(InputInt)  # 转换为整数
InputFloat = float(inputStr)
print(InputFloat)  # 转换为浮点数
