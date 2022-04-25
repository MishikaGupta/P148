# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:51:01 2022

@author: Beautiful Mishika
"""

from tkinter import *
import random

root=Tk()
root.title("PICNIC BAG LIST")
root.geometry("400x400")

Label_1 = Label(root) 
Label_2 = Label(root)

list = ["Bottle, Chips, Tickets, Hanky, Tiffin, Id Card, Chocolates"]

Label_1["text"] = "Lists Item :- " + str(list)

def randomlist() :
    randomlist = random.sample(range(0,6),1)
    Label_2["text"] = "Put item number " + str(randomlist) + " in the bag."
    
btn=Button(root,text="Which item to put in the bag?", command=randomlist)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

Label_1.place(relx=0.5, rely=0.3, anchor=CENTER)
Label_2.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
    