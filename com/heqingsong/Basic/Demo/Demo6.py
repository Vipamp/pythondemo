# -*- coding: utf-8 -*-
'''
Created on 2017年12月15日下午5:03:18
@author: HeQingsong
'''

#    字符串处理
#    使用''或者""都可以表示字符串，使用\表示转义字符

str = 'Runoob'
 
print (str)  # 输出字符串
print (str[0:-1])  # 输出第一个到倒数第二个的所有字符    Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
print (str[0])  # 输出字符串第一个字符
print (str[2:5])  # 输出从第三个开始到第五个的字符
print (str[2:])  # 输出从第三个开始的后的所有字符
print (str[2:10])  # 输出从第三个开始的后的所有字符
print (str * 2)  # 重复连接字符串
print (str + "TEST")  # 连接字符串
# 拼接字符串
str2 = "Hello ""ptyhon!"
str3 = "Hello " + "ptyhon!" 
print(str2)
print(str3)

print('Ru\noob')         
print(r'Ru\noob')  # 如果字符串中的\不当做转义字符输出，需要在引号前面加上r，表示原始字符串

#    Python 没有单独的字符类型，一个字符就是长度为1的字符串。
#    Python 字符串不能被改变，不能改指定的索引位赋值，比如word[0] = 'm'会导致错误。
