'''
Author: Jose Luis Balcazar, 2022 - ORCID 0000-0003-4248-4528 
Copyleft: MIT License (https://en.wikipedia.org/wiki/MIT_License)

Browsing through Countries by Area; areas as of 2018, 
data source: Our World in Data.

Simple tkinter-based GUI.

Current country kept as an index ("finger") of the list.

The buttons' callbacks are here implemented as closures.
'''


from json import load
import tkinter 
from tkinter.messagebox import showerror # requires separate import

gui = tkinter.Tk(className = " Browsing through Countries by Area")

def set_data(n_entry, a_entry, datafile):
	'''
	Initialize sorted list and create closures to be used as
	button callbacks. Each closure modifies the finger, hence 
	nonlocal declaration needed. Entries are also modified via
	methods but not assigned: nonlocal declaration not needed.
	'''

	finger = None

	with open(datafile) as df:
		areas = load(df)
		areas = sorted(areas.items(), key = lambda x: x[1])

	def query():
		nonlocal finger
		finger = None
		a_entry.delete(0, tkinter.END)
		i = 0
		while i < len(areas) and finger is None:
			"linear search"
			if areas[i][0] == n_entry.get():
				finger = i
			i += 1
		if finger is not None:
			a_entry.insert(0, areas[finger][1])
		else:
			showerror("Error", "Country " + n_entry.get() + " not found")
			n_entry.delete(0, tkinter.END)

	def up():
		nonlocal finger
		if finger is not None and finger < len(areas) - 1: 
			finger += 1
			n_entry.delete(0, tkinter.END)
			a_entry.delete(0, tkinter.END)
			n_entry.insert(0, areas[finger][0])
			a_entry.insert(0, areas[finger][1])

	def down():
		nonlocal finger
		if finger is not None and finger > 0: 
			finger -= 1
			n_entry.delete(0, tkinter.END)
			a_entry.delete(0, tkinter.END)
			n_entry.insert(0, areas[finger][0])
			a_entry.insert(0, areas[finger][1])

	return query, up, down


"set up entries and labels"
n_entry = tkinter.Entry(gui)
n_entry.grid(row=0, column=0)
a_entry = tkinter.Entry(gui)
a_entry.grid(row=0, column=1)
label = tkinter.Label(gui, text = " sq. kms              ")
label.grid(row=0, column=2)

"create closures and bind them as button callbacks"
query, up, down = set_data(n_entry, a_entry, 'areas.json')

b = tkinter.Button(gui, text="Refresh", command=query)
b.grid(row=0,column=3)
b = tkinter.Button(gui, text="Up", command=up)
b.grid(row=0,column=4)
b = tkinter.Button(gui, text="Down", command=down)
b.grid(row=0,column=5)


gui.mainloop()
