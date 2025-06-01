'''
Very simple conversion tool to demonstrate tkinter

This version: feb 2022
'''

# import tkinter 
from tkinter import *

gui = Tk()

label_meters = Label(gui, text="Enter meters")
label_meters.grid(row=0, column=0)
e_meters = Entry(gui)
e_meters.grid(row=0, column=1, columnspan=2)

label_or = Label(gui, text="or")
label_or.grid(row=1, column=0)

label_yards = Label(gui, text="Enter yards")
label_yards.grid(row=2, column=0)
e_yards = Entry(gui)
e_yards.grid(row=2, column=1, columnspan=2)

def y2m():
    "convert yards to meters"
    e_meters.delete(0, END)
    e_meters.insert(0, float(e_yards.get()) * 0.9144)
        
def m2y():
    "convert meters to yards"
    e_yards.delete(0, END)
    e_yards.insert(0, float(e_meters.get()) / 0.9144)

b_up = Button(gui, text="yards to meters   ^", command=y2m)
b_up.grid(row=1,column=1)
b_down = Button(gui, text="v   meters to yards", command=m2y)
b_down.grid(row=1,column=2)

gui.mainloop()


