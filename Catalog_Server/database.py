import sqlite3 as sql
import os

init_objects = [
	{
		'Title': 'How to get a good grade in DOS in 40 minutes a day',
		'Topic': 'Distributed Systems',
		'Quantity': 3,
		'Price': 120
	},
	{
		'Title': 'RPCs for Noobs',
		'Topic': 'Distributed Systems',
		'Quantity': 3,
		'Price': 70
	},
	{
		'Title': 'Xen and the Art of Surviving Undergraduate School',
		'Topic': 'Undergraduate School',
		'Quantity': 3,
		'Price': 100
	},
	{
		'Title': 'Cooking for the Impatient Undergrade',
		'Topic': 'Undergraduate School',
		'Quantity': 3,
		'Price': 65
	},
]

def create_db():
	if os.path.exists('database.sqlite'):
		print('Database Exists')
		return
	else:
		conn = sql.connect('database.sqlite')
		conn.execute('CREATE TABLE Book(id INTEGER PRIMARY KEY AUTOINCREMENT, Title TEXT NOT NULL, Topic TEXT NOT NULL, Quantity INTEGER NOT NULL, Price INTEGER NOT NULL)')
		
		cursor = conn.cursor()
		
		# Store the initial objects in the database
		for item in init_objects:
			cursor.execute(
				'INSERT INTO Book(Title, Topic, Quantity, Price) VALUES(?, ?, ?, ?)', 
				(item["Title"], item["Topic"], item["Quantity"], item["Price"])
			)
			conn.commit()
		
		conn.close()
		print('Database Created')
