import sqlite3 as sql
import json
from errors_handlers import *
from flask import abort, request

# Fetch book by ID
def info(book_id):
	
	# If the id is not number => 422
	if not book_id.isnumeric():
		abort(422)
	
	book_fetched = {}
	try:
		# Try to connect to SQLite DB
		conn = sql.connect('database.sqlite')
		cursor = conn.cursor()
		# Fetch one row
		result = cursor.execute('SELECT * FROM Book WHERE id = ?', (book_id,)).fetchone()
		
		# If the book exists
		if result is not None:
			book_fetched = {
				#"id": result[0],
				"title": result[1],
				"topic": result[2],
				"quantity": result[3],
				"price": result[4]
			}
		# Else, not found
		else:
			abort(404)
		
		cursor.close()
		
	except sql.Error as err:
		print("Failed to read single row from Book table.")
	
	finally:
		if conn:
			conn.close()
	
	# Return the data as JSON-String formatted
	return json.dumps(book_fetched)
	

# Search for book by topic
def search(topic):
	books_fetched = []
	try:
		# Try to connect to SQLite DB
		conn = sql.connect('database.sqlite')
		cursor = conn.cursor()
		# Fetch all books
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

	# Return as JSON-String formatted
	return json.dumps(book_fetched)
		

# Update book by ID
def update(book_id, quantity):
	book_updated = {}
	try:
		# Try to connecto to SQLite DB
		conn = sql.connect('database.sqlite')
		cursor = conn.cursor()
		# Update the book in DB
		cursor.execute('UPDATE Book SET Quantity = ? WHERE id = ?', (quantity, book_id,))
		# Commit
		conn.commit()
		
		# Get the book after updating it
		result = cursor.execute('SELECT * FROM Book WHERE id = ?', (book_id,)).fetchone()
		
		if result is not None:
			book_updated = {
				#"id": result[0],
				"title": result[1],
				"topic": result[2],
				"quantity": result[3],
				"price": result[4]
			}
		else:
			abort(404)
		
		cursor.close()
		
	except sql.Error as err:
		print("Failed to update single row in Book table.")
	
	finally:
		if conn:
			conn.close()

	return json.dumps(book_updated)
	
	
# Update book info by ID
def updateInfo(book_id, quantity, price):
	book_updated = {}
	try:
		# Try to connecto to SQLite DB
		conn = sql.connect('database.sqlite')
		cursor = conn.cursor()
		# Update the book in DB
		print(price, quantity)
		cursor.execute('UPDATE Book SET Quantity = ?, Price = ? WHERE id = ?', (quantity, price, book_id,))
		# Commit
		conn.commit()
		
		# Get the book after updating it
		result = cursor.execute('SELECT * FROM Book WHERE id = ?', (book_id,)).fetchone()
		
		if result is not None:
			book_updated = {
				#"id": result[0],
				"title": result[1],
				"topic": result[2],
				"quantity": result[3],
				"price": result[4]
			}
		else:
			abort(404)
		
		cursor.close()
		
	except sql.Error as err:
		print("Failed to update single row in Book table.")
	
	finally:
		if conn:
			conn.close()

	return json.dumps(book_updated)	

