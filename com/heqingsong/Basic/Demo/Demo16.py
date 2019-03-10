# -*- coding: utf-8 -*-
'''
Created on 2018年5月23日下午1:40:47
@author: HeQingsong
@description:    判断字符串中是否有重复字符
'''


def isDuplicateList(list_a):    
    for i in range(0, len(list_a) // 2 - 1):
        if list_a.count(list_a[i]) > 1:
            return True
    return False


list_a = ['a', 'b', 'a', 'd', 'e']
ret = isDuplicateList(list_a)
print("list_a id duplicate list?{}".format(ret))
