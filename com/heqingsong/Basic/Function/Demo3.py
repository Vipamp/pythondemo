# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:56
   @File Name：Demo3.py
   @Python Version: 3.6 by Anaconda
   @Description：函数的传值与传引用的问题
'''

'''
    传值和传引用的问题：
    string, tuple        ：是不可更改的对象，在函数中不可更改
    list,dict            ：是可以修改的对象，在函数里面修改后，可以把修改后的值带回来
    number               ：是不可更改对象，但是每次修改，都是换一次引用（指向的地址），修改后的值不能带回来
    备注：其理解思路和java一样，list和dict类型都是引用，
        列表和字典是引用，当参数传递在方法中修改后，是可以带回来的
'''


#    修改整数
def ChangeInt(a):
    a = 10


b = 2
ChangeInt(b)
print(b)  # 结果是 2


#    修改List
def changeList(list):
    for i in range(5):
        list[i] = i


list = list(range(5, 10))
print(list)
changeList(list)
print(list)  # 结果是[1,2,3,4,5]


#    修改Dict
def changeDict(dict):
    dict['age'] = 20


dict = {'Name': 'Hqs', 'age': '24'}
print(dict)
changeDict(dict)
print(dict)  # age的结果是20
