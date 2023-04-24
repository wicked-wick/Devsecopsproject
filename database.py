import csv
import sqlite3
with open('devsecops_players_22.csv','r',encoding='utf-8') as players:
	players_rec=csv.reader(players)
	conn=sqlite3.connect('football.db')
	cursor=conn.cursor()
	cursor.execute('''CREATE TABLE IF NOT EXISTS playerstb (id INTEGER PRIMARY KEY,
								name TEXT,
								Age INTEGER,
								nationality TEXT,
								overall INTEGER,
								potential INTEGER,
								club_name TEXT,
								position TEXT,
								photo TEXT)''')
	for row in players_rec:
		conn.execute('''Insert into playerstb(name,Age,nationality,overall,potential,club_name,position,photo) 
				values(?,?,?,?,?,?,?,?)''',(row[0],row[1],row[2],row[3],row[4],row[5],row[8],row[9]))
	conn.commit()
	conn.close()

