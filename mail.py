#为社么我打错了文件名

from time import *

from tkinter import *

mainwindow=Tk()
mainwindow.geometry('1000x260')
lan=StringVar()
def bt1c():
    #第一个按钮的执行
    lan.set(open('e:\\main_files\\xiwolocker\\save.txt').read())
def bt2c():
    #第2个按钮的执行
    open('e:\\main_files\\xiwolocker\\save.txt',mode="a").write(en1.get())
    lan.set(open('e:\\main_files\\xiwolocker\\save.txt').read())
def bt3c():
    open('e:\\main_files\\xiwolocker\\save.txt',mode="w").write('')
    lan.set(open('e:\\main_files\\xiwolocker\\save.txt').read())
bt1=Button(text='read',command=bt1c)
bt1.place(x=20,y=20)
lb1=Label(textvariable=lan,wraplength=700)
lb1.place(x=200,y=50)
bt2=Button(text="write",command=bt2c)
bt2.place(x=20,y=50)
en1=Entry()
en1.place(x=20,y=70)
bt3=Button(text='clean',command=bt3c)
bt3.place(x=20,y=100)
mainwindow.mainloop()

