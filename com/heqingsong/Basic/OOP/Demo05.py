# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/24 17:18
   @File Name：Demo05.py
   @Python Version: 3.6 by Anaconda
   @Description：父子类方法的重写和属性的访问关系
'''

'''
    类的继承和方法重写
     1、子类可以继承父类的方法和属性
     2、子类在写构造方法时，必须先调用父类的构造方法，否则子类对象调用父类方法或者属性时会报错
     3、子类可以重写父类的方法，调用该方法时，子类对象执行子类的方法，父类对象执行父类的方法
     4、子类可以调用父类的成员方法，也可以调用自己的成员方法：
                     调用父类方法：父类类名.方法名(self,……)
                     调用子类方法：self.方法名(……)
                     一般如果不在父子类里面调用方法，上面的两种方法调用结果一样，如果是在子类调用方法，两种方法结果不一样，
                     需要区分调用父类的方法还是子类方法
     5、子类直接继承父类的属性，可以直接通过self.属性名     访问
'''


class Person:

    def __init__(self, name='name'):
        self.name = name

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def speak(self):
        print("I am a Person")

    def toString(self):
        return 'My name is ' + self.name


class Student(Person):

    def __init__(self, name, studyId):
        Person.__init__(self, name)  # 在子类的构造方法中，必须先调用父类的构造方法，否则无法绑定父类的方法和属性，子类调用父类方法时会报错
        self.studyId = studyId

    # 子类重写父类的方法，也可以调用父类的方法
    def speak(self):
        Person.speak(self)
        print("I am a student")

    def toString(self):
        self.speak()
        return 'My name is ' + self.name + ",and My studyId is :" + self.studyId


student = Student('HQS', '1305011016')
print(student.toString())
print(student.getName())
print("子类调用自己的方法：")
student.speak()
person = Person()
print("父类调用自己的方法：")
person.speak()
