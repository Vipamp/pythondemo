# -*- coding: utf-8 -*-
'''
Created on 2017年12月15日下午5:03:18
@author: HeQingsong
'''
#    模块导入

#    1、导入整个模块
import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为', sys.path)
print()

#    2、导入模块的某个成员
from sys import argv, path  #  导入特定的成员
 
print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path
print('argv:', argv)