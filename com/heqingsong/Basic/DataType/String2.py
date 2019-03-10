# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:27
   @File Name：String2.py
   @Python Version: 3.6 by Anaconda
   @Description：String字符串的高级操作
'''
from builtins import type

# 1、使用%格式化
str = 'Hello %s,my name is %s' % ('world', 'HeQingsong')
print(str)

# 2、字符串模板格式化
from string import Template

tem = Template('Hello $name,my name is $name2')
str2 = tem.substitute(name='world', name2='HeQingsong')
print(str2)

# 3、查询子串的位置，如果可以查到，返回首字母所在索引，如果没有返回-1
str1 = 'hello World'
print(str1.find('World'))
print(str1.find('world'))

# 4、find，如果出现多次，只返回第一次出现的位置
str2 = 'hi boy hi girl'
print(str2.find('hi'))  # 默认从母字符串首查找
print(str2.find('hi', 3))  # 从第3个位置开始向后找
print(str2.find('hi', 3, 10))  # 在3-10的位置查找

# 5、join，将list元素按照固定格式连接成字符串,list元素不能为数字,join和split是逆方法
list = ['1', '2', '3', '4', '5']
print(' + '.join(list))
print(' , '.join(list))

# 6、lower，字符串转换为小写
str3 = 'HELLO WORLD!'
str4 = str3.lower()
print(str4)

# 7、replace,子字符串替换，translate只替换单个字符
str5 = 'hello world,hello friend'
str6 = str5.replace('hello', 'hi')
print(str6)

# 8、split，返回结果是个list
str7 = '1+2+3+4+5'
strs = str7.split('+')
print(strs)
print(type(strs))

# 9、strip，去除两边的空格
str8 = ' hello HQS '
print(str8.strip())
