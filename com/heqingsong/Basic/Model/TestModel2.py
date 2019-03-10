# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/24 17:03
   @File Name：TestModel2.py
   @Python Version: 3.6 by Anaconda
   @Description：将引入的模块本地化调用
'''

#    将模块的方法和属性本地化
import com.heqingsong.Basic.Model.myModel as myModel

add = myModel.add
sub = myModel.sub
mul = myModel.mul
div = myModel.div

#    在本地直接使用方法名调用方法
print(add(1, 3))
print(sub(1, 3))
print(mul(1, 3))
print(div(1, 3))
