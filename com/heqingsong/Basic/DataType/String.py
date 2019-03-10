# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:23
   @File Name：String.py
   @Python Version: 3.6 by Anaconda
   @Description：String字符串的基本操作
'''

#    声明并赋值一个字符串，可以使用单引号，也可以使用双引号
str1 = 'Hello Python2.0!'
str2 = "Hello Python3.0!"

#    可以使用\作为转义字符
str3 = "Hello \nPython"  # 使用\n换行
str4 = r"Hello \nPython"  # 在字符串前面使用r标识，字符串的\不当做转义字符使用
print("str3:", str3)
print("str4:", str4, "\n\n")

#    访问、截取字符串,
print(str1[0])
print(str1[0:-1])
print(str1[2:5])
print(str1[3:])
print(str1[:3])

#    字符串一旦确定，不允许改变，str1[2]='s'错误

#     常用转义字符：
#                     转义字符                    描述
#         \(在行尾时)     续行符
#         \\            反斜杠符号
#         \'            单引号
#         \"            双引号
#         \a            响铃
#         \b            退格(Backspace)
#         \e            转义
#         \000          空
#         \n            换    行
#         \v            纵向制表符
#         \t            横向制表符
#         \r            回车
#         \f            换页
#         \oyy          八进制数，yy代表的字符，例如：\o12代表换行
#         \xyy          十六进制数，yy代表的字符，例如：\x0a代表换行
#         \other        其它的字符以普通格式输出
#         
#         
#         
#     字符串操作
#        操作符            描述                                                                    实例
#         +      字符串连接                                           a + b 输出结果： HelloPython
#         *    重复输出字符串                                        a*2 输出结果：HelloHello
#         []    通过索引获取字符串中字符                   a[1] 输出结果 e
#         [ : ]    截取字符串中的一部分                   a[1:4] 输出结果 ell
#         in    成员运算符 - 如果字符串中包含给定的字符串返回 True    H in a 输出结果 1
#         not in    成员运算符 - 如果字符串中不包含给定的字符返回 True    M not in a 输出结果 1
#         r/R    原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。    print r'\n' prints \n 和 print R'\n' prints \n
#         %    格式字符串    

str5 = "String5  "
str6 = "String6  "
str7 = str5 + str6
print(str7)
print(str5 * 3)
print(str5 in str7)
print(str5 not in str6)
print(len(str5))  # 获取字符串长度

#    字符串格式化，和C语言中的printf相似
str = "\n\n我叫 %s 今年 %d 岁!" % ('小明', 10)
print(str)

#    """  """允许字符串跨行格式化
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)

# 原字符串：如果在字符串中使用转义字符等特殊字符，前面加上r取消转义
str = "Hello \nWorld!"
print(str)
str = r"Hello \nWorld!"
print(str)
