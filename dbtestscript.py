import sqlite3
conn=sqlite3.connect('football.db')
c=conn.cursor()
c.execute('Select * from playerstb')
records = c.fetchall()
for r in records:
	print(r)
conn.close()

