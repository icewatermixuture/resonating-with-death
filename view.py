import tkinter
import tkinter.font as tkFont
from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import sqlite3
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Inp(Frame):  #添加信息主体
    def __init__(sf, ma=None):  
        Frame.__init__(sf, ma)  
        sf.re = ma  #添加内部变量
        sf.t1 = Entry(sf)
        sf.t2 = Entry(sf)
        sf.t3 = Entry(sf)
        sf.t4 = Entry(sf)
        sf.t5 = Entry(sf)
        sf.t6 = Entry(sf)
        sf.Page()  

    def Iss(sf,tx):#确认表是否为空
        tp = 0
        for j in tx:
           if not j.isspace():
               tp = 1
               break;
        if tp==1:
            return 0
        else:
            return 1


    def write(sf,na,nm,cs,sc):#添加信息流程
        g = open('Grade.csv','r',encoding='utf-8')
        for line in g.readlines():
            info = line[:-1].split(",")
            if len(info)<4:
                break
            if info[1] ==nm and info[2] ==cs:
                 messagebox.showinfo(title='结果', message ="已存在该信息！")
                 g.close()
                 return

        g.close()
        g = open('Grade.csv','a',encoding='utf-8')
        g.write('{},{},{},{}\n'.format(na,nm,cs,sc))
        g.close()
        messagebox.showinfo(title='提示', message ="添加成功")
        conn= sqlite3.connect("new.db")#得分点1使用数据库
        df = pd.read_csv('Grade.csv')
        df.to_sql('new', conn, if_exists='append', index=False)
        return
    
    def click(sf):#确认输入的信息
        na = sf.t1.get()
        nm = sf.t2.get()
        cs = sf.t3.get()
        sc = sf.t4.get()
        if sf.Iss(na) or sf.Iss(nm) or sf.Iss(cs) or sf.Iss(sc) :
            messagebox.showinfo(title='提示', message ="输入项为空")
        else:
            sf.write(na,nm,cs,sc)
            
        
        
    def Page(sf):  #添加信息界面
        Label(sf).grid(row=0, stick=W, pady=10)
        a = '#090085'
        b='#ffffff'
        ft = tkFont.Font(family='Times New Roman', size=12, weight=tkFont.BOLD)
        sf.page = Frame(sf.re,bg='#d2fcff')
        sf.page.pack(expand=YES,fill=BOTH)
        Label(sf, text = '姓名: ',font=ft,bg=a,fg=b).grid(row=1, stick=W, pady=10)
        sf.t1.grid(row=1, column=1, stick=E)

        Label(sf, text = '学号: ',font=ft,bg=a,fg=b).grid(row=2, stick=W, pady=10)
        sf.t2.grid(row=2, column=1, stick=E)

        Label(sf, text = '科目: ',font=ft,bg=a,fg=b).grid(row=3, stick=W, pady=10) 
        sf.t3.grid(row=3, column=1, stick=E) 

        Label(sf, text = '成绩: ',font=ft,bg=a,fg=b).grid(row=4, stick=W, pady=10)
        sf.t4.grid(row=4, column=1, stick=E)       
        
        Button(sf, text='录入',command=sf.click,font=ft,bg=a,fg=b).grid(row=6, column=1, stick=E, pady=10)


        

class Del(Frame):  #删除信息主体
    def __init__(sf, ma=None):  
        Frame.__init__(sf, ma)  
        sf.re = ma 
        sf.t1 = Entry(sf)
        sf.t2 = Entry(sf)
        sf.Page()
        
    def Iss(sf,tx):#确认表是否为空
        tp = 0
        for j in tx:
           if not j.isspace():
               tp = 1
               break;
        if tp==1:
            return 0
        else:
            return 1

    def delete(sf,nm,cs):#删除信息流程
        temp = 0
        with open("Grade.csv","r",encoding="utf-8") as f:
            lines = f.readlines()
   
        with open("Grade.csv","w",encoding="utf-8") as f_w:
            for line in lines:
                info = line[:-1].split(",")
                if info[1] ==nm and info[2] ==cs:
                    temp = 1
                    
                    continue
                f_w.write(line)
                
        if temp==0:
            messagebox.showinfo(title='提示', message ="没有该信息")
        else:
            messagebox.showinfo(title='提示', message ="删除成功")
        
    def click(sf):#确认输入的信息
        nm = sf.t1.get()
        cs = sf.t2.get()
        if sf.Iss(nm) or sf.Iss(cs):
            messagebox.showinfo(title='提示', message ="输入项为空")
        else:
            sf.delete(nm,cs)
            
    def Page(sf):#删除信息界面
        a = '#090085'
        b = '#ffffff'
        ft = tkFont.Font(family='Times New Roman', size=12, weight=tkFont.BOLD) 
        sf.page = Frame(sf.re,bg='#d2fcff')
        Label(sf).grid(row=0, stick=W, pady=10)     
        Label(sf, text = '学号: ',font=ft,bg=a,fg=b).grid(row=1, stick=W, pady=10)
        sf.t1.grid(row=1, column=1, stick=E)
        Label(sf, text = '科目: ',font=ft,bg=a,fg=b).grid(row=2, stick=W, pady=10)
        sf.t2.grid(row=2, column=1, stick=E)
        Button(sf, text='删除',command=sf.click,font=ft,bg=a,fg=b).grid(row=6, column=1, stick=E, pady=10)   
  
class Mod(Frame):   #更改信息主体
    def __init__(sf, ma=None):  
        Frame.__init__(sf, ma)  
        sf.re = ma  
        sf.t1 = Entry(sf)
        sf.t2 = Entry(sf)
        sf.t3 = Entry(sf)
        sf.t4 = Entry(sf)
        sf.t5 = Entry(sf)
        sf.Page()  

    def Iss(sf,tx):#确认表是否为空
        tp = 0
        for j in tx:
           if not j.isspace():
               tp = 1
               break;
        if tp==1:
            return 0
        else:
            return 1
        
    def modify(sf,na,nm,cs,sc):#更改信息流程
        temp = 0
        with open("Grade.csv","r",encoding="utf-8") as f:
            lines = f.readlines()
   
        with open("Grade.csv","w",encoding="utf-8") as f_w:
            for line in lines:
                info = line[:-1].split(",")
                if info[1] ==nm and info[2] ==cs:
                    temp = 1
                    f_w.write('{},{},{},{}\n'.format(na,nm,cs,sc))
                    continue
                f_w.write(line)
        if temp==0:
            messagebox.showinfo(title='提示', message ="没有该信息")
        else:
            messagebox.showinfo(title='提示', message ="修改成功")
        
    def click(sf):#确认输入的信息
        na = sf.t1.get()
        nm = sf.t2.get()
        cs = sf.t3.get()
        sc = sf.t4.get()
        if sf.Iss(na) or sf.Iss(nm) or sf.Iss(cs) or sf.Iss(sc) :
            messagebox.showinfo(title='提示', message ="输入项为空")
        else:
            sf.modify(na,nm,cs,sc)  
    def Page(sf):  #更改信息界面
        a = '#090085'
        b = '#ffffff'
        ft = tkFont.Font(family='Times New Roman', size=12, weight=tkFont.BOLD)        
        Label(sf).grid(row=0, stick=W, pady=10)
        Label(sf, text = '姓名: ',font=ft,bg=a,fg=b).grid(row=1, stick=W, pady=10)
        sf.t1.grid(row=1, column=1, stick=E)
        Label(sf, text = '学号: ',font=ft,bg=a,fg=b).grid(row=2, stick=W, pady=10)
        sf.t2.grid(row=2, column=1, stick=E)
        Label(sf, text = '科目: ',font=ft,bg=a,fg=b).grid(row=3, stick=W, pady=10) 
        sf.t3.grid(row=3, column=1, stick=E) 
        Label(sf, text = '成绩: ',font=ft,bg=a,fg=b).grid(row=4, stick=W, pady=10)
        sf.t4.grid(row=4, column=1, stick=E)    
        Button(sf, text='修改',font=ft,bg=a,command=sf.click,fg=b).grid(row=6, column=1, stick=E, pady=10)   
class Que(Frame): #查询主体 
    def __init__(sf, ma=None):  
        Frame.__init__(sf, ma)  
        sf.re = ma 
        sf.t1 = Entry(sf)
        sf.t2 = Entry(sf)
        sf.Page()  

    def Iss(sf,tx):#确认表是否为空
        tp = 0
        for j in tx:
           if not j.isspace():
               tp = 1
               break;
        if tp==1:
            return 0
        else:
            return 1

    def query(sf,nm,cs):#查询流程
        w = open('Grade.csv','r',encoding='utf-8')
        for line in w.readlines():
            info = line[:-1].split(",")
            if info[1] ==nm and info[2] ==cs:
                 messagebox.showinfo(title='结果', message ="姓名："+info[0] +"\n学号:"+info[1] +"\n科目:"+info[2] +"\n成绩:"+info[3] )
                 w.close()
                 return

        messagebox.showinfo(title='提示', message ="没有该信息")
        w.close()
        return       
        
        
    def click(sf):#确认输入的信息
        nm = sf.t1.get()
        cs = sf.t2.get()
        if sf.Iss(nm) or sf.Iss(cs):
            messagebox.showinfo(title='提示', message ="输入项为空")
        else:
            sf.query(nm,cs)
            
            
    def Page(sf):#查询界面
        Label(sf).grid(row=0, stick=W, pady=10)
        a = '#090085'
        b='#ffffff'
        ft = tkFont.Font(family='Times New Roman', size=12, weight=tkFont.BOLD)         
        Label(sf, text = '学号: ',font=ft,bg=a,fg=b).grid(row=1, stick=W, pady=10)
        sf.t1.grid(row=1, column=1, stick=E)
        Label(sf, text = '科目: ',font=ft,bg=a,fg=b).grid(row=2, stick=W, pady=10)
        sf.t2.grid(row=2, column=1, stick=E)
        Button(sf, text='查找',command=sf.click,font=ft,bg=a,fg=b).grid(row=6, column=1, stick=E, pady=10)
          
class Sor(Frame):#排名
    def __init__(sf, ma=None):  
        Frame.__init__(sf, ma)  
        sf.re = ma 
        sf.t1 = Entry(sf)
        sf.Page()  

    def Iss(sf,tx):#确认表是否为空
        tp = 0
        for j in tx:
           if not j.isspace():
               tp = 1
               break;
        if tp==1:
            return 0
        else:
            return 1

    def sort(sf,cs):#排名流程
        s = pd.read_csv('Grade.csv')
        math = (s['Subject']==cs)
        exe = s[math].sort_values(by='Grade')#得分点6，使用pandas包，并使用数据切片技术。
        re = tkinter.Tk(className=" 成绩表 ")
        textPad = ScrolledText(re, width=50, height=50)
        textPad.insert(tkinter.constants.END, chars = str(exe))
        textPad.pack()
        re.mainloop()
    def click(sf):#确认输入的信息
        cs = sf.t1.get()
        if sf.Iss(cs):
            messagebox.showinfo(title='提示', message ="输入项为空")
        else:
            sf.sort(cs)
            
            
    def Page(sf):#排名界面
        a = '#090085'
        b='#ffffff'
        ft = tkFont.Font(family='Times New Roman', size=12, weight=tkFont.BOLD)
        Label(sf).grid(row=0, stick=W, pady=10)
        Label(sf, text = '科目: ',font=ft,bg=a,fg=b).grid(row=1, stick=W, pady=10)
        sf.t1.grid(row=1, column=1, stick=E)
        Button(sf, text='查找',command=sf.click,font=ft,bg=a,fg=b).grid(row=5, column=1, stick=E, pady=10)
class Ana(Frame):  #成绩分析主体
    def __init__(sf, master=None):  
        Frame.__init__(sf, master)  
        sf.re = master 
        sf.t1 = Entry(sf)
        sf.Page()  
    def Iss(sf,tx):#确认表是否为空
        tp = 0
        for j in tx:
           if not j.isspace():
               tp = 1
               break;
        if tp==1:
            return 0
        else:
            return 1
    def sort(sf,cs):#分析画图流程
        s = pd.read_csv('Grade.csv')
        ma = (s['Subject']==cs)
        exe = s[ma].sort_values(by='Grade')
        a = []
        good = 0
        qualified = 0
        failed = 0
        for dev in exe['Grade']:  # 读取数据
            if dev >= 90:
                good += 1
            elif (dev >= 60 and dev < 90):
                qualified += 1
            else:
                failed += 1
        lb = ['Good', 'Qualified', 'Failed']
        va = [good, qualified, failed]
        co = ['#00f90b', '#f9f800', '#f10b00']
        ex = [0, 0, 0]
        plt.title("成绩分析饼图", fontsize=25) #得分点2使用matplotlib绘图方法
        plt.pie(va, labels=lb, explode=ex, colors=co,startangle=180,shadow=False, autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()
        
    def click(sf):#确认输入的信息
        cs = sf.t1.get()
        if sf.Iss(cs):
            messagebox.showinfo(title='提示', message ="输入项为空")
        else:
            sf.sort(cs)  
    def Page(sf):#成绩分析界面
        Label(sf).grid(row=0, stick=W, pady=10)
        a = '#090085'
        b='#ffffff'
        ft = tkFont.Font(family='Times New Roman', size=12, weight=tkFont.BOLD)        
        Label(sf, text = '科目: ',font=ft,bg=a,fg=b).grid(row=1, stick=W, pady=10)
        sf.t1.grid(row=1, column=1, stick=E)
        Button(sf, text='查找',command=sf.click,font=ft,bg=a,fg=b).grid(row=5, column=1, stick=E, pady=10) 
class Che(Frame):#查找学生主体
    def __init__(sf, ma=None):  
        Frame.__init__(sf, ma)  
        sf.re = ma 
        sf.t1 = Entry(sf)
        sf.Page()  

    def Iss(sf,tx):#确认表是否为空
        tp = 0
        for j in tx:
           if not j.isspace():
               tp = 1
               break;
        if tp==1:
            return 0
        else:
            return 1

    def check(sf,na):#查找学生流程
        s = pd.read_csv('Grade.csv',encoding='utf-8')
        nm = (s['Name']==na)
        exe = s[nm].sort_values(by='Grade')
        re = tkinter.Tk(className=" GradeCheck！")
        textPad = ScrolledText(re, width=50, height=40)
        textPad.insert(tkinter.constants.END, chars = str(exe))
        textPad.pack()
        re.mainloop()
    def click(sf):#确认输入的信息
        na = sf.t1.get()
        if sf.Iss(na):
            messagebox.showinfo(title='提示', message ="输入项为空")
        else:
            sf.check(na)    
    def Page(sf):#查找学生界面
        a = '#090085'
        b='#ffffff'
        ft = tkFont.Font(family='Times New Roman', size=12, weight=tkFont.BOLD)  
        Label(sf).grid(row=0, stick=W, pady=10)
        Label(sf, text = '姓名: ',font=ft,bg=a,fg=b).grid(row=1, stick=W, pady=10)
        sf.t1.grid(row=1, column=1, stick=E)
        Button(sf, text='查找',command=sf.click,font=ft,bg=a,fg=b).grid(row=6, column=1, stick=E, pady=10) 
