import sqlite3
from json import dump

sql_query = "SELECT name, area FROM areas"

a = dict()

with sqlite3.connect("areas.db") as db_connection:
	res = db_connection.execute(sql_query)
	for name, area in res:
		a[name] = area
with open("areas.json", "w") as f:
	dump(a, f)


