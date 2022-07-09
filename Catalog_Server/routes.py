from book import info, search, update
from flask_application import app


# Get info about a book
def get_info(book_id):
	return info(book_id)


# Get all books about specific subject/topic
def get_books_related_to_topic(book_topic):
	return search(book_topic)



queries = {
	'query-by-item': {
		'function': get_info
	},
	'query-by-subject': {
		'function': get_books_related_to_topic
	}
}


# Get query and filter it
@app.route('/<string:query>/<parameter>', methods=['GET'])
def queryFromDB(query, parameter):
	if query not in queries:
		return 'Invalid query method has been called called', 404
	
	return queries[query]['function'](parameter)


# Update an book according to specific ID
@app.route('/update/<int:book_id>', methods=['PUT'])
def update_book(book_id):
	data = request.json
	
	if data is None:
		data = {}
	
	if data.get('Quantity') is None or data.get('Price') is None:
		abort(400)

	book = update(book_id, data.get('Quantity'), data.get('Price'))
		
	return book
