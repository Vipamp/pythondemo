# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/19 18:45
   @File Name：Loop_for.py
   @Python Version: 3.6 by Anaconda
   @Description：for循环语句
'''

'''
    range函数：
        1、range（num）：生成从 0 到 num-1 的序列
        2、range（num1,num2）：生成从 num1到 num2-1的序列
        3、range（num1,num2,step）：生成从 num1到 num2-1的序列，步长为step
          可以把range()函数获取到的结果当成序列看待，也可以使用range()创建一个列表
'''
listTemp = list(range(2, 5))
print(listTemp)

'''
    for循环格式：
        for 循环中间变量 in 集合：
                                循环体
        [else:
                                循环体]
        else

    for循环体中可以使用break、continue，效果和java一致，如果使用break跳出循环体，else语句的内容也不会执行
'''
print("\n")
for i in [1, 2, 3, 4, 5]:  # python没有像java的那种for循环，直接是遍历集合，这是最简单的写法，可以理解成java的增强型循环
    print(i, end=",")

print("\n")
for i in range(5):  # 生成 0-4的序列    等同于 for i in list(range(5))
    print(i, end=",")

print("\n")
for i in range(5, 10):  # 生成5-9的序列     等同于 for i in list(range(5,10))
    print(i, end=",")

print("\n")
for i in range(5, 10, 2):  # 生成 5-9，步长为2的序列F的序列, 等同于 for i in list(range(5,10,2))
    print(i, end=",")

print("\n")
for i in "Hello World":
    print(i, end=",")

# 遍历List
print("\n");
list = ["C", "C++", "Java", "Python"];
for i in list:
    print(i, end=",")

# 或者
print("\n")
for i in range(len(list)):
    print(i, list[i])

# 遍历tuple
tu = (1, 2, 3, 4, 5)
print('\n')
for x in tu:
    print(x, end=',')

# 遍历dict，注意遍历dict时，遍历的元素是dict的key，而不是key-value键值对entry
print('\n')
dict = {'name': 'HQS', 'age': 23}
for key in dict:
    print(key, "--->", dict[key])
