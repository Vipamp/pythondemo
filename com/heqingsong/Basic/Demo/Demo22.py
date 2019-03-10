import math
import random
from tkinter import *

allmoney = 0.0  # 红包总金额
allNum = 0  # 红包总数量
extMoney = 0.0  # 红包剩余金额
extNum = 0  # 红包剩余数量
list_dict = {}  # 领取红包名单和红包金额
user_dict = {}  # 用户名和密码
user_pack_dict = {}  # add  保存发的红包人名称和收红包人列表对应关系，就是每个用户给那些人发送过红包
user_money_num_dict = {}  # 保存每个人发送红包的剩余数量和金额        顺序：红包总金额_总数量_剩余金额_剩余数量
curName = ""  # 当前接收红包这个人的名称
curMoney = 0.0  # 当前接收红包的金额
user = ""  # 当前登录的用户名
account_dict = {}
moneyWaitForGet = 0.0  # 当前用户待领取的红包金额
sendMoneyUser = ""  # 当前待领取红包的发送人


# 确认生成红包
def run1():
    global allmoney, allNum, extMoney, extNum, allMoneyInput, allNumInput, lb61, lb60, user
    allmoney = float(allMoneyInput.get())
    allNum = int(allNumInput.get())
    
    if user in user_money_num_dict:
        showMessage("上次剩余红包未发完，请先将上次的红包发放完")
    else:
        # 检查账户余额是否充足
        if(allmoney > float(account_dict[user])):
            showMessage("账户余额不充足")
        else:
            extMoney = allmoney
            extNum = allNum
            lb60.configure(text='红包剩余金额{}元'.format(extMoney))
            lb61.configure(text="剩余数量{}个".format(extNum))
            account_dict[user] = float(account_dict[user]) - allmoney 


# 给指定好友发送红包
def run2():
    global extMoney, extNum, curMoney, curName, curNameInput, lb60, lb61, lb50, lb51
    curName = curNameInput.get()
    if(curName in list_dict):
        showMessage("已经给%s发送了%.2f的红包，把这个红包给他人吧，雨露均沾嘛！" % (curName, float(list_dict[curName].split("_")[0])))
    else:
        if curName in user_dict:
            if(extNum == 0):
                # 红包已发完
                showMessage("你的红包已经发完")
            else:
                # 红包未发完
                if(extNum == 1):
                    curMoney = extMoney
                else:
                    # 生成红包随机数
                    flag = True
                    while(flag):
                        # 产生随机整数和2位随机小数
                        curMoney = random.randint(0, int(extMoney)) + float("%.2f" % (random.random()))
                        if(curMoney >= 0.01 and curMoney < extMoney - (extNum - 1) * 0.01):
                            flag = False
                # 修改红包信息
                extNum -= 1
                extMoney -= curMoney
                lb60.configure(text='红包剩余金额%.2f元' % (extMoney))
                lb61.configure(text="剩余数量%d个" % (extNum))
                lb50.configure(text='已给 %s' % (curName))
                lb51.configure(text='发送红包%.2f元' % (curMoney))
                list_dict[curName] = str(curMoney)
                
                # 保存剩余红包金额和数量信息
                if extNum > 0:
                    user_money_num_dict[user] = str(allmoney) + "_" + str(allNum) + "_" \
                                                + str(extMoney) + "_" + str(extNum)
                else:
                    if user in user_money_num_dict:
                        del user_money_num_dict[user];
                
                # 保存user和发红包列表的信息
                user_pack_dict[user] = list_dict
        else:
            showMessage(curName + " 不在好友列表中，无法给他发送红包")

        
# 导出发送红包列表到指定文件
def save():
    global list_dict, allmoney, allNum, extMoney, extNum, fileOutputNameInput, account_dict, user
    filename = fileOutputNameInput.get()
    if(filename == ""):
        showMessage("请输入导出文件名称")
    else:
        f = open(filename + ".txt", 'w', encoding='utf-8')
        mg = user + "发送红包，总金额：%.2f，已发送红包数%d，剩余金额%.2f元的红包未发送" % (allmoney, allNum - extNum, extMoney)
        f.write(mg + "\n" + "====================================================\n")
        for key in list_dict.keys():
            s = list_dict[key].split("_")  # 获取每个红包的接收人key对应的 金额、是否已领取的信息,[0]是金额，[1]是领取状况
            if (len(s) == 1):
                # 该红包未领取
                message = "%s:%.2f元，待领取\n" % (key, float(s[0]))
            else:
                money = float(s[0])
                state = ""
                if(int(s[1]) == 1):
                    message = "%s:%.2f元，对方已领取\n" % (key, float(s[0]))
                else:
                    message = "%s:%.2f元，对方拒绝领取，红包金额已返回到您的账户上\n" % (key, float(s[0]))
            f.write(message)
        f.close()
        showMessage("导出文件成功")


# 保存账户信息到指定文件中
def saveAccount():
    global account_dict, user, extMony
    f = open("account.txt", 'w', encoding='utf-8')
    for key in account_dict.keys():
        f.write("%s：%.2f\n" % (key, float(account_dict[key])))
    f.close()   


# 显示提示信息窗口
def showMessage(message):
    root = Tk()
    mg = Label(root, text=message, fg='red')
    mg.pack()
    root.mainloop()


# 返回到登录页面
def back():
    global list_dict
    del list_dict
    saveAccount()
    subWindow.destroy()
    show1()


# 显示登录页面的标签
def show1():
    global window, loginUserlb, inputUser, loginPwdlb, inputPwd, loginButton
    window = Tk()
    window.title("登录")
    window.geometry("400x200")
    
    loginUserlb = Label(window, text="用户名：")
    inputUser = Entry(window)
    loginPwdlb = Label(window, text="密码：")
    inputPwd = Entry(window)
    loginButton = Button(window, text='登录', command=login)
    
    loginUserlb.grid(column=0, row=0)
    inputUser.grid(column=1, row=0)
    loginPwdlb.grid(column=0, row=1)
    inputPwd.grid(column=1, row=1)
    loginButton.grid(column=1, row=2)
    
    window.mainloop()


# 打开发红包界面
def show2():
    checkPack()
    
    global subWindow, lb0, lb10, allMoneyInput, lb12, lb20, allNumInput, lb22, button, lb40
    global curNameInput, button2, lb50, lb51, lb60, lb61, lb70, fileOutputNameInput, button3, backButton
    global allmoney, allNum, extMoney, extNum, list_dict, user_dict, curName, curMoney
        
    curName = ""  # 当前接收红包这个人的名称
    curMoney = 0.0  # 当前接收红包的金额
    list_dict = {}
    
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
    
    # 查看上次有没有剩余红包
    if user in user_money_num_dict:
        money_num = user_money_num_dict[user].split("_")
        allmoney = float(money_num[0])  # 红包总金额
        allNum = int(money_num[1])  # 红包总数量
        extMoney = float(money_num[2])  # 红包剩余金额
        extNum = int(money_num[3])  # 红包剩余数量
        lb60.configure(text='红包剩余金额%.2f元' % (float(extMoney)))
        lb61.configure(text="剩余数量%d个" % (int(extNum)))
        list_dict = user_pack_dict[user]
        showMessage("上次红包有剩余，请先发送剩余红包")
    else:
        allmoney = 0.0  # 红包总金额
        allNum = 0  # 红包总数量
        extMoney = 0.0  # 红包剩余金额
        extNum = 0  # 红包剩余数量
        if(user in user_pack_dict):
            list_dict = user_pack_dict[user]  # 领取红包名单和红包金额

    subWindow.mainloop()


# 查看有没有收到红包：
def checkPack():
    global user_pack_dict, user
    global moneyWaitForGet, sendMoneyUser  # 待领取的红包金额和发送人
    for key in user_pack_dict.keys():
        list = user_pack_dict[key]
        if user in list:
            # 领到了红包：
            s = list[user]
            if(len(s.split("_")) == 1):
                # 如果等于1，说明这个红包之前没有领过或者拒绝过，这里不再重复领取
                moneyWaitForGet = float(s)
                sendMoneyUser = key
                getPackOrNot('收到了%s的红包%.2f元，是否确认领取' % (key, float(moneyWaitForGet)))


# 确认是否领红包
def getPackOrNot(message):
    global  getPackRoot
    getPackRoot = Tk()
    lb = Label(getPackRoot, text=message)
    lb.pack()
    
    sureBtn = Button(getPackRoot, text='确认领取', command=sureGet)
    sureBtn.pack()
    
    cancelBtn = Button(getPackRoot, text='拒绝领取', command=cancelGet)
    cancelBtn.pack()
    getPackRoot.mainloop()


# 确认领取红包
def sureGet():
    global getPackRoot, moneyWaitForGet
    account_dict[user] += moneyWaitForGet  # 领取红包，加载自己的账户上
    user_pack_dict[sendMoneyUser][user] = str(user_pack_dict[sendMoneyUser][user]) + "_1"  # _1表示红包已领取
    getPackRoot.destroy()
    showMessage("红包已领取")
    saveAccount()

    
# 拒绝领取红包
def cancelGet():
    global  getPackRoot, moneyWaitForGet
    account_dict[sendMoneyUser] += moneyWaitForGet  # 拒绝红包，钱退还给发送者的账户
    user_pack_dict[sendMoneyUser][user] = str(user_pack_dict[sendMoneyUser][user]) + "_0"  # _1表示红包已退还
    getPackRoot.destroy()
    showMessage("红包已退还给%s" % (sendMoneyUser))
    saveAccount()


# 登录
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
window.title("登录")
window.geometry("400x200")
    
loginUserlb = Label(window, text="用户名：")
inputUser = Entry(window)
loginPwdlb = Label(window, text="密码：")
inputPwd = Entry(window)
loginButton = Button(window, text='登录', command=login)
    
loginUserlb.grid(column=0, row=0)
inputUser.grid(column=1, row=0)
loginPwdlb.grid(column=0, row=1)
inputPwd.grid(column=1, row=1)
loginButton.grid(column=1, row=2)
  
window.mainloop()

subWindow = Tk()
subWindow.title("发送随机红包小程序")
subWindow.geometry("450x300")

getPackRoot = Tk()
getPackRoot.title("红包领取确认")
getPackRoot.geometry("200x300")

