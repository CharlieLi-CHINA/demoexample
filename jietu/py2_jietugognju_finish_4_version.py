# -*- coding: utf-8 -*-
"""
fuction  A small tool that automatically screenshots and saves
finish date 20170906
vision  py2_jietugognju_test_4_version
author  Charlie Li
解决问题：能自动命名截图，采取的是随机数的方法，即10000以内的随机数
"""
from Tkinter import *
from PIL import ImageGrab
import random
class Jietu:
    def __init__(self, master): #
        
        frame = Frame(master)#
        frame.pack()
        self.label = Label(text="您好，这是个简单的全屏截图工具",fg="blue").pack(fill=BOTH) 
        self.labe2 = Label(text="截图文件自动保存在D盘的“jietu“文件夹",fg="blue").pack(fill=BOTH) 
        self.labe3 = Label(text="所以截图前请保证在d盘建立一个名字为 jietu 的文件夹",fg="blue").pack(fill=BOTH)
        self.labe4 = Label(text="您可以自主命名截图文件，也可以直接截图",fg="blue").pack(fill=BOTH)
        #there is to tell others the fuction of the programe
        self.label2 = Label(text="这里可以命名截图文件",fg="orange").pack(side=LEFT,fill=BOTH)
        self.entry = Entry(master)
        self.entry.pack(side=LEFT)
       
        self.screenshot=Button(master, text="截图", bd=6,bg='yellow',fg='red',font='10',command=self.jietu)
        #bg设置按键背景颜色，fg设置按键文字颜色，font设置按键中的字体大小，bd设置按键的边框大小
        self.screenshot.pack(anchor=CENTER)
       
        
    #this function is how to screeshot and to save the picture
    def jietu(self): 
        strsjs = str(random.randint(0,10000))
        pic = ImageGrab.grab()
        if self.entry.get():          
             pic.save("D:\\"+"jietu\\"+self.entry.get()+".jpg")
             print "Where the pictrue save is in :"+"D:\\"+"jietu\\"+self.entry.get()+".jpg"
        else:
            pic.save("D:\\"+"jietu\\"+strsjs+".jpg")
            print "Where the pictrue save is in :"+"D:\\"+"jietu\\"+strsjs+".jpg"

        
    #this function is to tell people whre the file saving in the commond windows
    
   
if __name__ == '__main__':#1
    root = Tk()#
    tool = Jietu(root)#
    root.mainloop()#