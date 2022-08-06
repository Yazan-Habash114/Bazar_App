import sqlite3 as sql
import os

# Initial books inserted to DB
init_objects = [
	{
		'Title': 'How to get a good grade in DOS in 40 minutes a day',
		'Topic': 'Distributed Systems',
		'Quantity': 3,
		'Price': 40
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
		'Price': 90
	},
	{
		'Title': 'Cooking for the Impatient Undergrade',
		'Topic': 'Undergraduate School',
		'Quantity': 3,
		'Price': 65
	},
	{
		'Title': 'How to finish Project 3 on time',
		'Topic': 'New Book',
		'Quantity': 3,
		'Price': 70
	},
	{
		'Title': 'Why theory classes are so hard',
		'Topic': 'New Book',
		'Quantity': 3,
		'Price': 45
	},
	{
		'Title': 'Spring in the Pioneer Valley',
		'Topic': 'New Book',
		'Quantity': 3,
		'Price': 30
	},
]

def create_db():
	# If the DB exists, return (Do not create new one)
	if os.path.exists('database.sqlite'):
		print('Database Exists')
		return
	else:
		# Create new DB
		conn = sql.connect('database.sqlite')
		# Create table
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
