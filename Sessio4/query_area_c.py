'''
Author: Jose Luis Balcazar, 2022 - ORCID 0000-0003-4248-4528 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Areas of countries as of 2018; data source: Our World in Data.

Simple tkinter-based GUI.

The button's callback is here implemented as a closure.
'''

from json import load
import tkinter 
from tkinter.messagebox import showerror # requires separate import

gui = tkinter.Tk(className = " Areas of Countries")

def make_query(n_entry, a_entry, datafile):
	'''
	To create the closure function having access to 
	data and both entries.
	'''
	
	with open(datafile) as df:
		areas = load(df)
		
	def query():
		'''
		The closure itself: accesses areas and n_entry (without 
		changing them), and modifies a_entry via its methods insert 
		and delete (no assignment: no need to declare it nonlocal).
		'''
		a_entry.delete(0, tkinter.END)
		name = n_entry.get() 
		if name in areas:
			a_entry.insert(0, areas[name])
		else:
			n_entry.delete(0, tkinter.END)
			showerror("Error", "Country " + name + " not found.")
	
	return query

"set up entries and labels"
n_entry = tkinter.Entry(gui)
n_entry.grid(row=0, column=0)
a_entry = tkinter.Entry(gui)
a_entry.grid(row=1, column=0)
label = tkinter.Label(gui, text = " sq. kms")
label.grid(row=1, column=1)

"create the closure and bind as button callback"
query = make_query(n_entry, a_entry, "areas.json")
b = tkinter.Button(gui, text="Query area of country", command=query) 
b.grid(row=0,column=1)

gui.mainloop()
