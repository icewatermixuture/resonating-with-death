import tkinter as tk
from tkinter import *
#from MainPage import *
from LoginPage import *

root = tk.Tk()
root.title('学生成绩管理系统')
photo = tk.PhotoImage(file="mj.jpg")
label_img = tk.Label(root,image=photo,bg='#E0FFFF')
label_img.pack(expand=YES,fill=BOTH)
LoginPage(root)
#MainPage(root)
root.mainloop()
