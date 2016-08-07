#!/usr/bin/python

from Tkinter import *
root = Tk()
# Code to add widgets will go here...
li = 'Red Green Blue Yellow'.split()
listb = Listbox(root)
for item in li:
    listb.insert(0,item)

listb.pack()
root.mainloop()
