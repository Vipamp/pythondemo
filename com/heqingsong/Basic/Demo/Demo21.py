# -*- coding: utf-8 -*-
'''
Created on 2018年6月9日下午5:13:56
@author: HeQingsong
@description:
'''
import math
import random
from tkinter import *

allmoney = 0.0  # 红包总金额
allNum = 0  # 红包总数量
extMoney = 0.0  # 红包剩余金额
extNum = 0  # 红包剩余数量
list_dict = {}  # 领取红包名单和红包金额
user_dict = {}  # 用户名和密码
curName = 0.0  # 当前接收红包这个人的名称
curMoney = 0.0  # 当前接收红包的金额
user = ""  # 当前登录的用户名
account_dict = {}


def run1():
    global allmoney, allNum, extMoney, extNum, allMoneyInput, allNumInput, lb61, lb60, user
    allmoney = float(allMoneyInput.get())
    allNum = float(allNumInput.get())
    # 检查账户余额是否充足
    if(allmoney > float(account_dict[user])):
        showMessage("账户余额不充足")
    else:
        extMoney = allmoney
        extNum = allNum
        lb60.configure(text='红包剩余金额{}元'.format(extMoney))
        lb61.configure(text="剩余数量{}个".format(extNum))
        account_dict[user] = float(account_dict[user]) - allmoney 


def run2():
    global extMoney, extNum, curMoney, curName, curNameInput, lb60, lb61, lb50, lb51
    curName = curNameInput.get()
    if(curName in list_dict):
        showMessage("已经给%s发送了%.2f的红包，把这个红包给他人吧，雨露均沾嘛！" % (curName, list_dict[curName]))
    else:
        if(extNum == 0):
            showMessage("你的红包已经发完")
        elif(extNum == 1):
            curMoney = extMoney
        else:
            flag = True
            while(flag):
                curMoney = random.randint(0, int(extMoney)) + random.random()
                if(curMoney >= 0.01 and curMoney < extMoney - (extNum - 1) * 0.01):
                    flag = False
        extNum -= 1
        extMoney -= curMoney
        lb60.configure(text='红包剩余金额%.2f元' % (extMoney))
        lb61.configure(text="剩余数量%d个" % (extNum))
        lb50.configure(text='已给 %s' % (curName))
        lb51.configure(text='发送红包%.2f元' % (curMoney))
        list_dict[curName] = curMoney
        if(curName in account_dict):
            account_dict[curName] += curMoney
        else:
            account_dict[curName] = curMoney


def save():
    global list_dict, allmoney, allNum, extMoney, extNum, fileOutputNameInput, account_dict, user
    global allMoneyInput, allNumInput, curNameInput, lb60, lb61, lb50, lb51
    global var1, var2, var3, var4
    filename = fileOutputNameInput.get()
    if(filename == ""):
        showMessage("请输入导出文件名称")
    else:
        f = open(filename + ".txt", 'w', encoding='utf-8')
        mg = user + "发送红包，总金额：%.2f，%d个好友已领，剩余金额%.2f元" % (allmoney, allNum - extNum, extMoney)
        if(extMoney > 0):
            mg += "已返回你的账户上"
        f.write(mg + "\n" + "====================================================\n")
        for key in list_dict.keys():
            f.write("%s:%.2f\n" % (key, float(list_dict[key])))
        f.close()
    
        account_dict[user] = account_dict[user] + extMoney
        f = open("account.txt", 'w', encoding='utf-8')
        for key in account_dict.keys():
            f.write("%s：%.2f\n" % (key, float(account_dict[key])))
        f.close()   

        # 清空页面上的输入
        allMoneyInput.delete(0, END)
        allNumInput.delete(0, END)
        curNameInput.delete(0, END)
        fileOutputNameInput.delete(0, END)
        lb60.configure(text='')
        lb61.configure(text='')
        lb50.configure(text='')
        lb51.configure(text='')
        
        showMessage("导出文件成功")


def showMessage(message):
    root = Tk()
    mg = Label(root, text=message, fg='red')
    mg.pack()
    root.mainloop()


def back():
    subWindow.destroy()
    show1()


# 显示登陆页面的标签
def show1():
    global window, loginUserlb, inputUser, loginPwdlb, inputPwd, loginButton
    window = Tk()
    window.title("登陆")
    window.geometry("400x200")
    
    loginUserlb = Label(window, text="用户名：")
    inputUser = Entry(window)
    loginPwdlb = Label(window, text="密码：")
    inputPwd = Entry(window)
    loginButton = Button(window, text='登陆', command=login)
    
    loginUserlb.grid(column=0, row=0)
    inputUser.grid(column=1, row=0)
    loginPwdlb.grid(column=0, row=1)
    inputPwd.grid(column=1, row=1)
    loginButton.grid(column=1, row=2)
    
    window.mainloop()


def show2():
    global subWindow, lb0, lb10, allMoneyInput, lb12, lb20, allNumInput, lb22, button, lb40
    global curNameInput, button2, lb50, lb51, lb60, lb61, lb70, fileOutputNameInput, button3, backButton
    global allmoney, allNum, extMoney, extNum, list_dict, user_dict, curName, curMoney
    
    allmoney = 0.0  # 红包总金额
    allNum = 0  # 红包总数量
    extMoney = 0.0  # 红包剩余金额
    extNum = 0  # 红包剩余数量
    list_dict = {}  # 领取红包名单和红包金额
    curName = 0.0  # 当前接收红包这个人的名称
    curMoney = 0.0  # 当前接收红包的金额
    
    subWindow = Tk()
    subWindow.title("发送随机红包小程序")
    subWindow.geometry("450x300")
    
    lb0 = Label(subWindow, text="发红包")
    lb10 = Label(subWindow, text="请输入红包金额：")
    allMoneyInput = Entry(subWindow)        
    lb12 = Label(subWindow, text="元")
    lb20 = Label(subWindow, text="请输入红包数量：")
    allNumInput = Entry(subWindow)
    lb22 = Label(subWindow, text="个")
    button = Button(subWindow, text="确认", command=run1)
    lb40 = Label(subWindow, text="请输入指定发送人：")
    curNameInput = Entry(subWindow)
    button2 = Button(subWindow, text="发送随机红包", command=run2)
    lb50 = Label(subWindow, text="", fg='blue')  # 显示当次红包发送信息
    lb51 = Label(subWindow, text="", fg='blue')  # 显示档次红包发送信息
    lb60 = Label(subWindow, text="", fg='red')  # 显示剩余红包金额和红包数量
    lb61 = Label(subWindow, text="", fg='red')  # 显示剩余红包金额红包剩余数量
    lb70 = Label(subWindow, text="请输入导出文件名称")
    fileOutputNameInput = Entry(subWindow)
    button3 = Button(subWindow, text="导出红包数据到指定文件", command=save)
    backButton = Button(subWindow, text="返回", command=back)
    
    lb0.grid(column=1, row=0)
    lb10.grid(column=0, row=1)
    allMoneyInput.grid(column=1, row=1)
    lb12.grid(column=2, row=1)
    lb20.grid(column=0, row=2)
    allNumInput.grid(column=1, row=2)
    lb22.grid(column=2, row=2)
    button.grid(column=1, row=3)
    lb40.grid(column=0, row=4)
    curNameInput.grid(column=1, row=4)
    button2.grid(column=2, row=4)
    lb50.grid(column=0, row=5)
    lb51.grid(column=1, row=5)
    lb60.grid(column=0, row=6)
    lb61.grid(column=1, row=6)
    lb70.grid(column=0, row=7)
    fileOutputNameInput.grid(column=1, row=7)
    button3.grid(column=2, row=7)
    backButton.grid(column=1, row=8)
    
    subWindow.mainloop()

    
def login():
    global inputUser, inputPwd, user_dict, user
    user = inputUser.get()
    pwd = inputPwd.get()
    if user in user_dict:
        if(pwd == user_dict[user]):
            window.destroy()
            show2()
        else:
            showMessage("密码错误")
    else:
        showMessage("用户名不存在")


def readUser():
    global user_dict
    
    f = open("user.txt", 'r', encoding='utf-8')
    for line in f.readlines():
        userpwd = line.split("\n")[0].split('：')
        user_dict[userpwd[0]] = userpwd[1]
    f.close()


def readAccount():
    global account_dict
    f = open("account.txt", 'r', encoding='utf-8')
    for line in f.readlines():
        userAccount = line.split("\n")[0].split('：')
        account_dict[userAccount[0]] = float(userAccount[1])
    f.close()
    print(account_dict)
    

readUser()
readAccount()

window = Tk()
window.title("登陆")
window.geometry("400x200")
    
loginUserlb = Label(window, text="用户名：")
inputUser = Entry(window)
loginPwdlb = Label(window, text="密码：")
inputPwd = Entry(window)
loginButton = Button(window, text='登陆', command=login)
    
loginUserlb.grid(column=0, row=0)
inputUser.grid(column=1, row=0)
loginPwdlb.grid(column=0, row=1)
inputPwd.grid(column=1, row=1)
loginButton.grid(column=1, row=2)
  
window.mainloop()

subWindow = Tk()
subWindow.title("发送随机红包小程序")
subWindow.geometry("450x300")

