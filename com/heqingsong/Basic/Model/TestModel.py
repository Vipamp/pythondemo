# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/24 17:01
   @File Name：TestModel.py
   @Python Version: 3.6 by Anaconda
   @Description：测试使用自定义的模块
'''

#    直接导入模块名，使用模块名计算
import com.heqingsong.Basic.Model.myModel as myModel

# 或者下面的导入方式，两种都可以
# from com.heqingsong.Basic.Model.myModel import myModel;

print(myModel.add(1, 3))
print(myModel.sub(1, 3))
print(myModel.mul(1, 3))
print(myModel.div(1, 3))
