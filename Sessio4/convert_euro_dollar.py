'''
Very simple conversion tool to demonstrate tkinter

This version: feb 2022
'''

import tkinter 

gui = tkinter.Tk()

label_euros = tkinter.Label(gui, text="Enter euros")
label_euros.grid(row=0, column=0)
e_euros = tkinter.Entry(gui)
e_euros.grid(row=0, column=1, columnspan=2)

label_or = tkinter.Label(gui, text="or")
label_or.grid(row=1, column=0)

label_dollars = tkinter.Label(gui, text="Enter dollars")
label_dollars.grid(row=2, column=0)
e_dollars = tkinter.Entry(gui)
e_dollars.grid(row=2, column=1, columnspan=2)

def d2e():
    "convert dollars to euros"
    e_euros.delete(0, tkinter.END)
    e_euros.insert(0, float(e_dollars.get()) * 0.92140)
        
def e2d():
    "convert euros to dollars"
    e_dollars.delete(0, tkinter.END)
    e_dollars.insert(0, float(e_euros.get()) / 0.92140)

b_up = tkinter.Button(gui, text="dollars to euros   ^", command=d2e)
b_up.grid(row=1,column=1)
b_down = tkinter.Button(gui, text="v   euros to dollars", command=e2d)
b_down.grid(row=1,column=2)

gui.mainloop()


