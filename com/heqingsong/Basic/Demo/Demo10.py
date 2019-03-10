# -*- coding: utf-8 -*-
'''
Created on 2018年3月22日下午7:30:35
@author: HeQingsong
@description:
'''

import turtle;
t = turtle.Pen()
t.pensize(2)
t.pencolor("green")
t.pensize(5)
for i in range(0, 360):
    t.seth (i)
    t.fd (1)
