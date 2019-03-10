# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/19 19:02
   @File Name：List.py
   @Python Version: 3.6 by Anaconda
   @Description：List当做堆栈和队列使用
'''

'''
    List：当做线性表使用
'''

#    当做堆栈使用
myStack = []
#    使用append方法项栈顶添加元素
myStack.append("1")
myStack.append("2")
myStack.append("3")
myStack.append("4")
myStack.append("5")
print(myStack)
#    使用pop方法从栈顶删除数据
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())

#    当做队列使用
from collections import deque  # 导入deque

myQueue = deque([])
#    使用append向deque里面添加数据
myQueue.append("1")
myQueue.append("2")
myQueue.append("3")
myQueue.append("4")
myQueue.append("5")
print(myQueue)
#    使用popleft从队列头删除数据
print(myQueue.popleft())
print(myQueue.popleft())
print(myQueue.popleft())
print(myQueue.popleft())
print(myQueue.popleft())
