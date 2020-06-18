import tkinter as tk
from tkinter import *
from login import *

tit = tk.Tk()
tit.title('学生成绩管理系统')
pho = tk.PhotoImage(file="mj.jpg")
label_img = tk.Label(tit,image=pho,bg='#d2fcff')
label_img.pack(expand=YES,fill=BOTH)
Login(tit)       #开始界面
tit.mainloop()
