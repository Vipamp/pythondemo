# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/24 17:15
   @File Name：Demo03.py
   @Python Version: 3.6 by Anaconda
   @Description：实例对象的创建类判断
'''


class Person:

    def __init__(self):
        pass

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


class Animal:

    def __init__(self):
        pass


person = Person()
animal = Animal()

# 判断对象是否是类的实例
if isinstance(person, Person):
    print("person是Person的对象")

if not isinstance(animal, Person):
    print("animal不是Person的对象")

# 查看对象是属于哪个类
print("person是属于类：", person.__class__)
