'''
Very simple conversion tool to demonstrate tkinter

This version: feb 2022
'''

import tkinter 

gui = tkinter.Tk()

label_meters = tkinter.Label(gui, text="Enter meters")
label_meters.grid(row=0, column=0)
e_meters = tkinter.Entry(gui)
e_meters.grid(row=0, column=1, columnspan=2)

label_or = tkinter.Label(gui, text="or")
label_or.grid(row=1, column=0)

label_yards = tkinter.Label(gui, text="Enter yards")
label_yards.grid(row=2, column=0)
e_yards = tkinter.Entry(gui)
e_yards.grid(row=2, column=1, columnspan=2)

def y2m():
    "convert yards to meters"
    e_meters.delete(0, tkinter.END)
    e_meters.insert(0, float(e_yards.get()) * 0.9144)
        
def m2y():
    "convert meters to yards"
    e_yards.delete(0, tkinter.END)
    e_yards.insert(0, float(e_meters.get()) / 0.9144)

b_up = tkinter.Button(gui, text="yards to meters   ^", command=y2m)
b_up.grid(row=1,column=1)
b_down = tkinter.Button(gui, text="v   meters to yards", command=m2y)
b_down.grid(row=1,column=2)

gui.mainloop()


