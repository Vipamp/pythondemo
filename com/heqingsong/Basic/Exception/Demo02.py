# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:39
   @File Name：Demo02.py
   @Python Version: 3.6 by Anaconda
   @Description：通过raise关键词抛异常
'''

# 抛异常
# 在方法内可以使用raise抛异常，如果异常没有使用try-except捕获，就将异常从方法体抛出来，向上抛到调用该方法的地方，直到被try-except捕获
# 如果一直没有捕获，就从python解释器抛出来到客户端上
def div(x, y):
    if y == 0:
        raise Exception('除数不能为0')  # 抛异常
    else:
        return x / y


a = int(input("请输入被除数"))
b = int(input("请输入除数"))
try:
    print("结果为:", div(a, b))
except Exception as e:
    print(e)


def div2(x, y):
    try:
        if y == 0:
            raise Exception('除数不能为0')  # 抛异常
        else:
            return x / y
    except Exception as e:  # 捕获try语句块内的异常
        print(e)


print(div2(a, b))
