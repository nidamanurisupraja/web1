import sqlite3
con=sqlite3.connect('mydb.db')
cur=con.cursor()
query='create table student(rollno text,name text,branch text,email text)'
try:
	cur.execute(query)
except Exception as e:
	print(e)
finally:
	print("Successfully created")
