# -*- coding: utf-8 -*-
'''
Created on 2018年5月23日下午1:54:04
@author: HeQingsong
@description:
'''

import random
fruits = ['香蕉', '草莓', '苹果', '梨子', '西瓜', '芒果', '葡萄']
dicts = {}
for i in  range(0, 100):
    fruit = fruits[random.randint(0, 6)]
    if(fruit in dicts.keys()):
        dicts[fruit] = dicts[fruit] + 1
    else:
        dicts[fruit] = 1

print(dicts)
    
