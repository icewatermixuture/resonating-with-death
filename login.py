from tkinter import *
from tkinter.messagebox import *
from main import *
import tkinter.font as tkFont
import string
class Login(object):
    def __init__(sf, master=None):
        sf.re = master 
        sf.re.geometry('%dx%d' % (350, 450)) #设置窗口为350,450
        sf.username = StringVar()
        sf.password = StringVar()
        sf.new()
    def new(sf):
        a = '#090085'
        b='#ffffff'
        c = tkFont.Font(family='Times New Roman', size=13, weight=tkFont.BOLD)
        sf.pg = Frame(sf.re,bg='#d2fcff') 
        sf.pg.pack(expand=YES,fill=BOTH)#创建页面
        Label(sf.pg).grid(row=0, stick=W)
        Label(sf.pg, text = '账号: ',font=c,bg=a,fg=b).grid(row=1, stick=N+S, padx=10,pady=5)
        Entry(sf.pg, textvariable=sf.username,width=25,).grid(row=1, column=1, stick=E)
        Label(sf.pg, text = '密码: ',font=c,bg=a,fg=b).grid(row=2, stick=N+S, pady=10,padx=10)
        Entry(sf.pg, textvariable=sf.password, show='*',width=25).grid(row=2, column=1, stick=E)
        Button(sf.pg, text='登陆', command=sf.Check,font=c,bg=a,fg=b).grid(row=3, column=0, pady=5)
        Button(sf.pg, text='注册', command=sf.rg,font=c,bg=a,fg=b).grid(row=3, column=1, pady=5)
        Button(sf.pg, text='退出', command=sf.pg.quit,font=c,bg=a,fg=b).grid(row=3, column=2, pady=5)
    def Check(sf):#账号密码检测
        n = sf.username.get()
        psd = sf.password.get()
        if sf.psd(n,psd):
            sf.pg.destroy()
            Main(sf.re)
        else:
            showinfo(title='error', message='账号或密码错误！')
    def nm(sf,str):#注册信息检测
        nm=list(string.ascii_letters)#得分点5, 使用列表
        for i in str:
            if i in nm:
                pass
            else:
                return False
        return True
    def psd(sf,n,psd):
        g = open('Password.csv','r',encoding='utf-8')
        for line in g.readlines():
            inf = line[:-1].split(",")
            if len(inf)<2:
                break
            if inf[0].strip()==n and  inf[1].strip()==psd :
                 g.close()
                 return True
        return False
    def rg(sf):#注册流程
        n = sf.username.get()
        psd = sf.password.get()
        if len(n)==0 or len(psd)==0:
            showinfo(title='error', message='账号密码为空！')
            return
        for j in psd:
            if j == ',' or j == ' ':
                showinfo(title='error', message='密码含有非法字符！')
                return
        if sf.nm(n):
            pass
        else:
            showinfo(title='error', message='账号含有非法字符！')
            return
        ps = open('Password.csv','r',encoding='utf-8')
        for line in ps.readlines():
            f = line[:-1].split(",")
            if len(f)<2:
                break
            if inf[0].strip()==name:
                 messagebox.showinfo(title='error', message ="已存在该用户信息！")
                 g.close()
                 return
        ps.close()
        ps = open('Password.csv','a',encoding='utf-8')
        ps.write('{},{}\n'.format(n,psd))
        ps.close()
        messagebox.showinfo(title='success', message ="注册成功！")
