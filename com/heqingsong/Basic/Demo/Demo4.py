# -*- coding: utf-8 -*-
'''
Created on 2017年12月15日下午5:03:18
@author: HeQingsong
'''

#    标准数据类型（Number）
#    支持：int、float、bool、complex(复数)
#    python2中没有boolean类型，用0和1表示
#    python3中有boolean类型，可以使用True、False，也可以使用1/0，可以和数字相加

a, b, c, d = 1, 2.0, True, 1 + 2j
e = 2 + 3j

#    使用type()方法获取变量的数据类型
print("a的数据类型为：" , type(a))
print("b的数据类型为：" , type(b))
print("c的数据类型为：" , type(c))
print("d的数据类型为：" , type(d))
print(d * e)

#    使用isinstance判断数据类型
print("a的数据类型为int：" , isinstance(a, int))
print("a的数据类型为int：" , isinstance(b, int))
print("c的数据类型为float：" , isinstance(c, float))
print("d的数据类型为complex：" , isinstance(d, complex))

#    del可以删除对象引用，类似于java的obj=null
del a, b
print("a的数据类型为int：" , isinstance(a, int))


#    type和isinstance的区别
#    type()不会认为子类是一种父类类型。
#    isinstance()会认为子类是一种父类类型。
class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))  # returns True
print(type(A()) == A)  # returns True
print(isinstance(B(), A))  # returns True
print(type(B()) == A)  # returns False

