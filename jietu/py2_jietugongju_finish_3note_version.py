# -*- coding: utf-8 -*-
"""
fuction  A small tool that automatically screenshots and saves
finish date 20170822
vision  py2_jietugongju_finish_3note_version
author  Charlie Li
"""
from Tkinter import *
from PIL import ImageGrab
class Jietu:
    def __init__(self, master): #
        
        frame = Frame(master)#
        frame.pack()
        self.label = Label(text="Welcome!This is a screenshot tool",fg="blue").pack() 
        #there is to tell others the fuction of the programe
        self.label2 = Label(text="Press enter the file name",fg="orange").pack(side=LEFT)
        self.entry = Entry(master)
        self.entry.pack(side=LEFT)
        #where the input is and enter the picture name
        self.button2 = Button(master, text="save the file number", width=10,padx=35, pady=10, command=self.callback)
        self.button2.pack()
        #there is to save the pciture nanme wher you have set
        self.button1=Button(master, text="screenshot", padx=10, pady=10,command=self.jietu)
        self.button1.pack()
        #there is to screeshot
    #this function is how to screeshot and to save the picture
    def jietu(self): 
        pic = ImageGrab.grab()
        if self.entry.get():
            pic.save("D:\\"+"jietu\\"+self.entry.get()+".jpg")
        else: 
            pic.save("D:\\"+"jietu\\"+"picture"+".jpg")
            
        #pic.save("D:\\"+"jietu\\"+self.entry.get()+".jpg")
        
    #this function is to tell people whre the file saving in the commond windows
    def callback(self):
        if self.entry.get():
            print "Where the pictrue save is in :"+"D:\\"+"jietu\\"+self.entry.get()+".jpg"
        else: 
            print "Where the pictrue save is in :"+"D:\\"+"jietu\\"+"picture"+".jpg"
   
if __name__ == '__main__':#1
    root = Tk()#
    tool = Jietu(root)#
    root.mainloop()#