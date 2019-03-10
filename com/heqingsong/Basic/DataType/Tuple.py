# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:28
   @File Name：Tuple.py
   @Python Version: 3.6 by Anaconda
   @Description：Tuple元组操作
'''
'''
    元组
         元组与列表类似，不同之处在于列表的元素可以修改，元组的元素不能修改。
         元组使用小括号，列表使用方括号。
         元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
'''
#    创建元组
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
tupEmpty = ()  # 创建空元组

#     获取元素，和字符串、列表一样
print(tup1[2])
print(tup1[2:])
print(tup1[1:3])
print(tup1[:3])

#    如果元组只有一个元素，要加上逗号
tupTemp = (10)  # 这里tupTemp就是一个int类型的变量，()当做运算符对待
print(type(tupTemp))
tupTemp = (10,)  # 这里tupTemp才是一个元组
print(type(tupTemp))

#    修改元素，注意：Tuple元素不能修改，但是可以拼接元组
tupAdd = tup1 + tup2
print(tupAdd)

#    删除元素，注意：Tuple元素不能删除元素，但是可以删除Tuple，
del tupAdd
# print(tupAdd);  # 这里会报错，提示tupAdd未定义

# 元组运算
print(len(tupTemp))
print(tup1 + tup2)  # 连接
print(tup1 * 4)  # 复制
print(1 in tup2)  # 元素是否存在

for x in tup1:  # for遍历
    print(x)

# list转换为元组
print(tuple([1, 2, 3]))

# 字符串转换为元组
print(tuple('hello'))
