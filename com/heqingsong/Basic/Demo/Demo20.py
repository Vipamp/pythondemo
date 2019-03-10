

from tkinter import *
import random
# 随机发放红包

allmoney = 0.0  # 红包总金额
allNum = 0  # 红包总数量
extMoney = 0.0  # 红包剩余金额
extNum = 0  # 红包剩余数量
getPeoperName = ''  # 红包领取人
curMoney = 0.0  # 红包该领取人领取的金额


# 随机分发
def randOut():
    global extMoney
    global extNum
    global getPeoperName
    global curMoney
    if(extNum == 1):
        curMoney = extMoney
    else:
        flag = True
        while(flag):
            curMoney = random.random()
            print(curMoney)
            print(extMoney)
            print(extNum)
            if(0 < curMoney and curMoney < extMoney - 0.01 * extNum):
                extMoney -= curMoney
                extNum -= 1
                flag = False
    print(getPeoperName + ":" + curMoney)

    
# 随机分发红包
def out():
    subWindow = Tk()
    subWindow.title("发红包")
    # 领取人   
    lb = Label(subWindow, text="领取人：")
    lb.grid(column=0, row=1)
    getName = Entry(subWindow)
    getName.grid(column=1, row=1)

    # 随机分发
    button = Button(subWindow, text="发红包", command=randOut)    
    button.grid(column=1, row=2)
    subWindow.mainloop()


# 设置红包的内容
def deserve():
    
    subWindow = Tk()
    subWindow.title("发红包")
    
    # 红包总金额：
    lb = Label(subWindow, text="红包金额")
    lb.grid(column=0, row=0)    
    moneyInput = Entry(subWindow)
    moneyInput.grid(column=1, row=0)
     
    # 红包数量    
    lb2 = Label(subWindow, text="红包数量")
    lb2.grid(column=0, row=1)
    numInput = Entry(subWindow)
    numInput.grid(column=1, row=1)
    
    global allmoney 
    allmoney = moneyInput.get()
    global allNum
    allNum = numInput.get()

    # 随机分发
    button = Button(subWindow, text="发红包", command=out)  
    button.grid(column=1, row=2)  
    subWindow.mainloop()


# 主界面设置
def initGUI():
    root = Tk()
    root.title("发红包")
    # 开始发红包：
    mainLabel = Button(root, text="开始发红包", command=deserve)
    mainLabel.pack()
    # 查看发红包记录
    mainLabel = Button(root, text="查看发红包记录", command=deserve)
    mainLabel.pack()
    root.mainloop()


if __name__ == '__main__':
    initGUI()
