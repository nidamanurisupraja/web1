import sqlite3,cgi
print("content-Type:text/html \r\n\r\n")
form=cgi.FieldStorage()
a=form.getvalue('rollno')
b=form.getvalue('name')
c=form.getvalue('branch')
d=form.getvalue('email')
con=sqlite3.connect('mydb.db')
cur=con.cursor()
query='insert into student values("'+a+'","'+b+'","'+c+'","'+d+'")'
try:
	cur.execute(query)
	con.commit()
except exception as e:
	print(e)
finally:
	print("Successfully inserted")
