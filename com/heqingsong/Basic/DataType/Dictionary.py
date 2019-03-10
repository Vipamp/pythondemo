# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:03
   @File Name：Dictionary.py
   @Python Version: 3.6 by Anaconda
   @Description：python的dictionary类型的基础内容
'''
'''
    字典：
        字典就是键值对，和java中的Map一样，格式和json格式类似
              格式：{}
             一个键值对，通过逗号分隔，键在左，值在右，
              值可以不唯一，键必须唯一，如果重复了，不会报错，后一个覆盖前一个
            字典可以无限嵌套
            字符串，元组是不可变的数据类型，可以作为键，其他的数据类型不能作为键
'''
#    新建一个字典
dict = {'Name': 'HeQingsong', 'Age': '24', 'School': 'HFUU'}

#    访问字典里的值
print("姓名：%s" % (dict['Name']))
print("年龄：%s" % (dict['Age']))
print("学校：%s" % (dict['School']))

#    增加键值对
dict['sex'] = '男'
print(dict)

#    修改字典
#    向字典里增加新值
dict['Addr'] = '上海市徐汇区襄阳南路'
print("地址：%s" % (dict['Addr']))
#    修改字典原有数据的值
dict['Name'] = 'HQS'
print("姓名：%s" % (dict['Name']))

#    删除键值对
#    删除单个键值对
del dict['School']
print(dict)
# 删除所有键值对
dict.clear()
print(dict)

#    删除字典项
del dict
