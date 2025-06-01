'''
Author: Jose Luis Balcazar, 2022 - ORCID 0000-0003-4248-4528 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Areas of countries as of 2018; data source: Our World in Data.

Simple tkinter-based GUI.

The button's callback is here implemented by an object method.
'''

from json import load
import tkinter 
from tkinter.messagebox import showerror # requires separate import

gui = tkinter.Tk(className = " Areas of Countries")

class Query:
	
	def __init__(self, n_entry, a_entry, datafile):
		'''
		Create a new object of class Query.
		Store provided entries and filename as object fields.
		'''
		self.n_entry = n_entry
		self.a_entry = a_entry
		with open(datafile) as df:
			self.areas = load(df)
	
	def query(self):
		'''
		The callback for the button, implemented as a method of 
		objects of class Query.
		'''
		self.a_entry.delete(0, tkinter.END)
		name = self.n_entry.get()
		if name in self.areas:
			self.a_entry.insert(0, self.areas[name])
		else:
			self.n_entry.delete(0, tkinter.END)
			showerror("Error", "Country " + name + " not found.")

	
"set up entries and labels"
n_entry = tkinter.Entry(gui)
n_entry.grid(row=0, column=0)
a_entry = tkinter.Entry(gui)
a_entry.grid(row=1, column=0)
label = tkinter.Label(gui, text = " sq. kms")
label.grid(row=1, column=1)

"create object of class Query that provides the callback as a method"
q = Query(n_entry, a_entry, "areas.json")
b = tkinter.Button(gui, text="Query area of country", command=q.query)
b.grid(row=0,column=1)

gui.mainloop()
