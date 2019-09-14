import sqlite3,cgi
print("content-Type:text/html \r\n\r\n")
form=cgi.FieldStorage()
a=form.getvalue('rollno')
con=sqlite3.connect('mydb.db')
cur=con.cursor()
query='delete from student where rollno="'+a+'"'
try:
	cur.execute(query)
	con.commit()
except exception as e:
	print(e)
finally:
	print("Successfully deleted")
