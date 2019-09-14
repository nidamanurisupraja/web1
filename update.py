import sqlite3
con=sqlite3.connect('vrsec.db')
cur=con.cursor()
query='update student set name="natasha" where rollno="178w1a1231"'
try:
    cur.execute(query)
    con.commit()
except Exception as e:
    print(e)
finally:
    print("Successfully updated")
