# -*- coding: utf-8 -*-
'''
   @Author：HeQingsong
   @Date：2018/9/22 14:40
   @File Name：Demo01.py
   @Python Version: 3.6 by Anaconda
   @Description：文件读写操作
'''

'''
    open方法的参数介绍：
        file:文件名：强制参数
        mode：模式：r-读，w-写，a-追加，b-追加，+：读写
        bufffering：是否缓存，0或者False表示不缓存，直接从硬盘中读取文件，1或者True表示有缓存，将文件加载到内存中操作，大于1表示缓冲区的大小，<0
                                                表示默认缓冲区大小        
'''

f = open('test.txt', mode='r+')
'''
    1、读文件
        (1)read()读取全部文件，
        (2)read(num)从当前游标向后读取num个字节的数据，每读取一次，游标向后移动一次
'''
print("按照字节数读取文件")
print(f.read(25))
print(f.read())

'''
    2、按行读取文件
'''
print("\n按行读取文件")
f = open('test.txt', mode='r+')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

'''
    3、写文件
'''
f = open('test.txt', mode='w')
f.write("""Hello World!
My Name is HQS!
I am a programmer!
I like programming!
""")
f.close()
