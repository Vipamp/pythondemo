# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 13:57
   @File Name：ListExpression.py
   @Python Version: 3.6 by Anaconda
   @Description：python的列表推导式
'''

'''
    列表推导式：
            列表推导式提供了从序列创建列表的简单途径。
            格式：
            [表达式   for 变量  in 列表名]
            [表达式   for 变量  in 列表名  if expression]
            将原来的列表，依据一定的条件和逻辑，生成一个新的列表
'''

list = [1, 2, 3, 4, 5];
print(list)  # [1, 2, 3, 4, 5]
list2 = [2 * x for x in list]
print(list2)  # [2, 4, 6, 8, 10]

list3 = [1, 2, "3", True, [1, 2, 3], 4 + 5j, False]
list4 = [x for x in list3 if isinstance(x, int)]  # 使用if作为过滤条件
print(list4)  # [1, 2, True]            #python中，True可以是1，False可以是0
'''
等同于：
tempList = []
for x in list3:
    if(isinstance(x,int)):
        tempList.append(x)
'''

#    本质：在for循环里面，一次调用方法，将其结果一次赋值给新的列表
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])  # ['banana', 'loganberry', 'passion fruit']
'''   等同于
listTemp = [];
for weapon in freshfruit:
    listTemp.append(weapon.strip());
'''
#    列表嵌套：
list5 = [[x, 2 * x] for x in list];
print(list5)  # [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10]]
'''
等同于：
tempList = []
for x in list:
    tempList.append([x,2*x]) 
'''

#    高级：
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
tempList = [x * y for x in vec1 for y in vec2]
print(tempList)  # [8, 6, -18, 16, 12, -36, 24, 18, -54]
'''等同于：
tempList.empty();
for x in vec1:
    for y in vec2:
        tempList.append(x * y);
'''
