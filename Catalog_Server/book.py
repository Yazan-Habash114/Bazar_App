import sqlite3 as sql
import json
from errors_handlers import *
from flask import abort

# Fetch book by ID
def info(book_id):
	
	if not book_id.isnumeric():
		abort(422)
	
	book_fetched = {}
	try:
		conn = sql.connect('database.sqlite')
		cursor = conn.cursor()
		result = cursor.execute('SELECT * FROM Book WHERE id = ?', (book_id,)).fetchone()
		
		if result is not None:
			book_fetched = {
				#"id": result[0],
				"title": result[1],
				"topic": result[2],
				#"quantitiy": result[3],
				"price": result[4]
			}
		#else:
		#	abort(404)
		
		cursor.close()
		
	except sql.Error as err:
		print("Failed to read single row from Book table.")
	
	finally:
		if conn:
			conn.close()

	return json.dumps(book_fetched)
	

# Search for book by topic
def search(topic):
	books_fetched = []
	try:
		conn = sql.connect('database.sqlite')
		cursor = conn.cursor()
		result = cursor.execute('SELECT * FROM Book WHERE Topic = ?', (topic,)).fetchall()
		book_fetched = [
			dict(
				#id=row[0],
				title=row[1],
				topic=row[2],
				#quantity=row[3],
				price=row[4]
			)
			for row in result
		]
		cursor.close()
		
	except sql.Error as err:
		print("Failed to read multiple rows from Book table.")
	
	finally:
		if conn:
			conn.close()

	return json.dumps(book_fetched)
		

# Update book by ID
def update(book_id, quantity, price):
	book_updated = {}
	try:
		conn = sql.connect('database.sqlite')
		cursor = conn.cursor()
		cursor.execute('UPDATE Book SET Quantity = ?, Price = ? WHERE id = ?', (quantity, price, book_id,))
		conn.commit()
		
		result = cursor.execute('SELECT * FROM Book WHERE id = ?', (book_id,)).fetchone()
		
		if result is not None:
			book_updated = {
				#"id": result[0],
				"title": result[1],
				"topic": result[2],
				#"quantitiy": result[3],
				"price": result[4]
			}
		#else:
		#	abort(404)
		
		cursor.close()
		
	except sql.Error as err:
		print("Failed to update single row in Book table.")
	
	finally:
		if conn:
			conn.close()

	return json.dumps(book_updated)
