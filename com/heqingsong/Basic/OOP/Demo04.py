# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/24 17:16
   @File Name：Demo04.py
   @Python Version: 3.6 by Anaconda
   @Description：类的构造与析构
'''


# 构造方法：因为python参数可选，所以不区分有参构造和无参构造，
# 析构方法：垃圾回收时或者手动使用del时调用，慎用
class Person:

    def __init__(self, name='name', age=1, sex='nan'):
        # 构造方法
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        # 析构方法，用来在垃圾回收时调用该方法，因为不知道什么时候回收，尽量避免使用
        print("删除对象", self, "成功")
        pass

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSex(self, sex):
        self.sex = sex

    def getSex(self):
        return self.sex

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def toString(self):
        return 'name:%s,age:%d,sex:%s' % (self.name, self.age, self.sex)


# 调用无参构造
person1 = Person()
print(person1.toString())

# 调用有参构造
person2 = Person('HQS', 23, '男')
print(person2.toString())

del person1
del person2
