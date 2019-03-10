# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/24 17:12
   @File Name：Demo01.py
   @Python Version: 3.6 by Anaconda
   @Description：python的面向对象基础
'''

'''
    创建一个类：
    1、方法中，一般默认是共有方法，外部可以访问
    2、如果不想让外部访问，方法名前面加上__，例：def __setName()，该类型的方法，其他模块不能使用import导入
    3、类可以写构造方法，方法名固定为：def __init__(self):
'''


class Person:

    age = 12

    def __init__(self):
        # 构造函数：__init__是固定写法，在创建对象时执行该方法
        self.name = "HQS"
        self.age = 17
        self.sex = "Nan"
        print("初始化成功")
    
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


person = Person()
print("Name:", person.getName())
print("Sex:", person.getSex())
print("Age:", person.getAge())

person.setName("HeQingsong")
person.setSex("男")

print("Name:", person.getName())
print("Sex:", person.getSex())
print("Age:", person.getAge())
print(person.name)

# 方法绑定
setage = person.setAge
getage = person.getAge

setage(16)
print(getage())

# 方法的另一种调用形式：类名.方法名(self,其他参数)：这种方式更容易理解类中的每一个方法都加上self作为参数
# 可以看做每一个方法都是java中的静态方法，可以直接使用类名调用，参数self为对象名
# 调用形式1：对象名.方法名(……)这里面的参数不需要加上对象本身
# 调用形式2：类名.方法名(self,……)这里面的参数第一个为对象本身
# 例如：person.setName('HQS')   等同于    Person.setName(person,'HQS')

Person.setName(person, 'HQS')
Person.setAge(person, 23)
Person.setSex(person, '男')
print("Name:", Person.getName(person))
print("Sex:", Person.getSex(person))
print("Age:", Person.getAge(person))
