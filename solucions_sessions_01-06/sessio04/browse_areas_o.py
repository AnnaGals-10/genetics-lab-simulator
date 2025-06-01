'''
Author: Jose Luis Balcazar, 2022 - ORCID 0000-0003-4248-4528 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Browsing through Countries by Area; areas as of 2018, 
data source: Our World in Data.

Simple tkinter-based GUI.

Current country kept as an index ("finger") of the list.

The buttons' callbacks are here implemented by an object's methods.
'''

from json import load

import tkinter 
from tkinter.messagebox import showerror # requires separate import

gui = tkinter.Tk(className = " Browsing through Countries by Area")

class BrowseCountries:

	def __init__(self, n_entry, a_entry, datafile):
		'''
		Initialize object with sorted list. Store provided entries 
		and filename as object fields.
		Later, define methods to be used as button callbacks
		'''
		self.n_entry = n_entry
		self.a_entry = a_entry
		self.finger = None
		with open(datafile) as df:
			self.areas = sorted(load(df).items(), key = lambda x: x[1])

	def query(self):
		self.finger = None
		self.a_entry.delete(0, tkinter.END)
		i = 0
		while i < len(self.areas) and self.finger is None:
			if self.areas[i][0] == n_entry.get():
				self.finger = i
			i += 1
		if self.finger is not None:
			self.a_entry.insert(0, self.areas[self.finger][1])
		else:
			showerror("Error", "Country " + self.n_entry.get() + " not found")
			self.n_entry.delete(0, tkinter.END)

	def up(self):
		if self.finger is not None and self.finger < len(self.areas) - 1: 
			self.finger += 1
			self.n_entry.delete(0, tkinter.END)
			self.a_entry.delete(0, tkinter.END)
			self.n_entry.insert(0, self.areas[self.finger][0])
			self.a_entry.insert(0, self.areas[self.finger][1])

	def down(self):
		if self.finger is not None and self.finger > 0: 
			self.finger -= 1
			self.n_entry.delete(0, tkinter.END)
			self.a_entry.delete(0, tkinter.END)
			self.n_entry.insert(0, self.areas[self.finger][0])
			self.a_entry.insert(0, self.areas[self.finger][1])

"set up entries and labels"
n_entry = tkinter.Entry(gui)
n_entry.grid(row=0, column=0)
a_entry = tkinter.Entry(gui)
a_entry.grid(row=0, column=1)
label = tkinter.Label(gui, text = " sq. kms              ")
label.grid(row=0, column=2)

"create BrowseCountries object and bind its methods as button callbacks"
brows = BrowseCountries(n_entry, a_entry, "areas.json")

b = tkinter.Button(gui, text="Refresh", command=brows.query)
b.grid(row=0,column=3)
b = tkinter.Button(gui, text="Up", command=brows.up)
b.grid(row=0,column=4)
b = tkinter.Button(gui, text="Down", command=brows.down)
b.grid(row=0,column=5)


gui.mainloop()
