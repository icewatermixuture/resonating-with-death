from tkinter import *  
from view import *  #导入子页面  
  
class Main(object):  
    def __init__(sf, ma=None):  
        sf.re = ma                              #定义一个内部变量 
        sf.re.geometry('%dx%d' % (400, 500)) #设置窗口大小  
        sf.create()  
    def create(sf):  
        sf.ip = Inp(sf.re)  
        sf.dl = Del(sf.re)
        sf.mod = Mod(sf.re)
        sf.qy = Que(sf.re) 
        sf.st = Sor(sf.re)
        sf.ana = Ana(sf.re)
        sf.ck = Che(sf.re)# 创建不同功能的子界面
        sf.ip.pack() #默认打开添加信息界面 
        mb = Menu(sf.re)  # 设置菜单 
        mb.add_command(label='添加信息', command = sf.inp)  
        mb.add_command(label='删除信息', command = sf.dele)  
        mb.add_command(label='更改信息', command = sf.modi)  
        mb.add_command(label='查询', command = sf.que)  
        mb.add_command(label='成绩排名', command = sf.sor)
        mb.add_command(label='成绩分析', command = sf.asis)
        mb.add_command(label='查找学生', command = sf.che)
        sf.re['menu'] = mb  
    def inp(sf):  #设置菜单动作
        sf.ip.pack()  
        sf.qy.pack_forget()  
        sf.dl.pack_forget()
        sf.mod.pack_forget() 
        sf.st.pack_forget()
        sf.ana.pack_forget()
        sf.ck.pack_forget()
    def dele(sf):  
        sf.ip.pack_forget()  
        sf.qy.pack_forget()  
        sf.dl.pack()
        sf.mod.pack_forget() 
        sf.st.pack_forget()
        sf.ana.pack_forget()
        sf.ck.pack_forget()
    def modi(sf):  
        sf.ip.pack_forget()  
        sf.qy.pack_forget()  
        sf.dl.pack_forget()
        sf.mod.pack() 
        sf.st.pack_forget()
        sf.ana.pack_forget()
        sf.ck.pack_forget()        
    def que(sf):  
        sf.ip.pack_forget()  
        sf.qy.pack()  
        sf.dl.pack_forget()
        sf.mod.pack_forget() 
        sf.st.pack_forget()
        sf.ana.pack_forget()
        sf.ck.pack_forget()
    def sor(sf):
        sf.ip.pack_forget()  
        sf.qy.pack_forget()  
        sf.dl.pack_forget()
        sf.mod.pack_forget() 
        sf.st.pack()
        sf.ana.pack_forget()
        sf.ck.pack_forget()
    def asis(sf):
        sf.ip.pack_forget()  
        sf.qy.pack_forget()  
        sf.dl.pack_forget()
        sf.mod.pack_forget() 
        sf.st.pack_forget()
        sf.ana.pack()
        sf.ck.pack_forget()
    def che(sf):
        sf.ip.pack_forget()  
        sf.qy.pack_forget()  
        sf.dl.pack_forget()
        sf.mod.pack_forget() 
        sf.st.pack_forget()
        sf.ana.pack_forget()
        sf.ck.pack()
