# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:12
   @File Name：Dictionary3.py
   @Python Version: 3.6 by Anaconda
   @Description：字典的高级应用
'''

# 1、字典嵌套(原则上，字典可以无限嵌套)
dic1 = {'name': 'HQS', 'age': 12}
dic2 = {'schoolName': 'HFUU', 'addr': 'AH'}

dic = {'stu': dic1, 'school': dic2}

print(dic)
print("stu.name:", dic['stu']['name'])
print("stu.age:", dic['stu']['age'])
print("school.schoolName:", dic['school']['schoolName'])
print("school.addr:", dic['school']['addr'])

# 2、字典格式化字符串
tem = """
<html>
    <head>
        <title>%(title)s</title>
    </head>
    <body>
        <p>%(test)s</p>
    </body>
</html>
"""
dic = {'title': 'HQSWeb', 'test': '这是正文'}
print(tem % dic)
