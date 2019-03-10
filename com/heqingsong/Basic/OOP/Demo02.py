# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/24 17:14
   @File Name：Demo02.py
   @Python Version: 3.6 by Anaconda
   @Description：类的多重继承
'''
'''
    　类的继承：
        １、可以知己在子类名后加上括号，填入父类类名
        ２、支持多重继承
'''


class Person:
    # 创建父类Person

    def __init__(self):
        self.name = "HeQingsong"
        self.age = 23

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age


class Subject:
    pass


class Student(Person, Subject):
    # 子类Student集成父类Person

    def __init__(self):
        self.studyId = "123"

    def setStudyID(self, studyId):
        self.studyId = studyId

    def getStudyId(self):
        return self.studyId
