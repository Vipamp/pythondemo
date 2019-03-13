# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:14
   @File Name：List.py
   @Python Version: 3.6 by Anaconda
   @Description：list数据结构
'''

#    创建一个列表
list = ['Google', 'Runoob', 1997, 2 + 2j]
print(list)

#    获取列表的元素，索引从0开始，其获取值的方式同字符串一样，[]里面填需要获取值的索引，
#    索引>=0，从左边开始数，从0开始表示第一个元素，第一个元素为0
#    索引<0，从右边开始数，从1开始表示最后一个元素，最后一个元素为-1，切片是也是小数在前，大数在后
print(list[2])
print(list[2:5])    
print(list[2:])  # ：后面的不写，默认到最后
print(list[:3])  # ：前面的不写，默认从最前面开始
print(list[2:-2])
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[1:9:2])  # 如果：后有第三个参数，为步长
print(list[9:1:-2])  # 如果：后有第三个参数，为步长，步长为复数，从后向前取数

# 序列相加
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list + list2)

#    初始化数量为10的空列表，
emptyList = [0] * 10  # 一般不使用[]初始化，使用0初始化更实际
print(emptyList)

#    初始化数量为10的空列表，
emptyList = [None] * 10  # 也可以使用None初始化
print(emptyList)

#    修改列表，（String和List的区别：String不能根据索引值修改，List可以根据索引值修改）
list[2] = 'Hello Python!'
print(list)
#    如果左边的list里面是一个范围，右边必须是[]或者字符串，否则报错，两边的list长度没有限制，但必须是list，注意区别
list[2:5] = ["The End", 1 + 2j]
print(list)
list[2:5] = "The End"
print(list)

#    删除列表元素，删除后，后面的元素会去填充该元素的位置，而不是空着置为None
del list[1]
print(list)

#    列表嵌套，类似于多维数组
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']
x = [a, b]
print(x)
print(x[0])
print(x[1])
print(x[0][3])
print(x[1][2])

'''
     常用方法：
        1    len(list)        列表元素个数
        2    max(list)        返回列表元素最大值
        3    min(list)        返回列表元素最小值
        4    list(seq)        将元组转换为列表        
        
        
        1    list.append(obj)        在列表末尾添加新的对象
        2    list.count(obj)        统计某个元素在列表中出现的次数
        3    list.extend(seq)        在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
        4    list.index(obj)        从列表中找出某个值第一个匹配项的索引位置
        5    list.insert(index, obj)        将对象插入列表
        6    list.pop(obj=list[-1])        移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
        7    list.remove(obj)        移除列表中某个值的第一个匹配项
        8    list.reverse()        反向列表中元素
        9    list.sort([func])       对原列表进行排序
        10    list.clear()        清空列表
        11    list.copy()        复制列表
'''
list = [1, 2, 'a', 'f', 9 + 10j]
print("列表的长度为：%d" % (len(list)))
list.append(9 + 10j)
print("9+10j出现得次数为：%d" % (list.count(9 + 10j)))
print("'a'的索引值为：%d" % (list.index('a', 0, len(list) - 1)))

# list排序，调用sort方法，默认从小到大排序，是直接给原列表排序，不是重新生成一个列表
# 如果reverse参数是True，从大到小排列，False是从小到大排列
list2 = [1, 3, 32, 6, 4, 35, 8, 4, 45, 14]
list2.sort(reverse=True)
print(list2)

# list排序，调用sorted方法，默认从小到大排序，是重新生成一个排序列表
list2 = [1, 3, 32, 6, 4, 35, 8, 4, 45, 14]
list3 = sorted(list2)
print(list3)

