from flask_application import app, abort, request
import requests
import json
from flask import jsonify

# Import replication
from replication import replication

# Import caches
from cache import lookup_cache, search_cache, SearchEntry


# Search query
@app.route('/search/<topic>', methods=['GET'])
def search_according_to_topic(topic):
	# Search in cache first
	if topic in search_cache:
		print('\nResult by topic fetched from search cache\n')
		return jsonify(search_cache.get(topic).search_result)


	# Call Catalog Server, get response
	catalog_ip, catalog_port = replication.get_catalog_info()
	response = requests.get(f'http://{catalog_ip}:{catalog_port}/query-by-subject/{topic}')
	
	msg = ""
	if response.status_code == 200:
		msg = f"All books related with topic ({topic}):"
		# Cache the search result
		search_cache.insert(topic, SearchEntry(response.json()))
		print('\nSearch Cache Obj:\nCache: ', search_cache.cache, '\nLRU_Queue: ', search_cache.lru_Q, '\n')
	else:
		msg = "Error! Cannot fetch book with ID"
	
	return response.text, response.status_code, response.headers.items()


# Info query
@app.route('/info/<id>', methods=['GET'])
def info_according_to_id(id):
	if not id.isnumeric():
		abort(422)
	
	# Search in cache first
	cached_book = lookup_cache.get(int(id))
	if cached_book is not None:
		print('\nResult by item(id) fetched from lookup cache\n')
		return cached_book
	
	# Call Catalog Server, get response
	catalog_ip, catalog_port = replication.get_catalog_info()
	response = requests.get(f'http://{catalog_ip}:{catalog_port}/query-by-item/{id}')
	
	msg = ""
	if response.status_code == 200:
		msg = f"Book with ID ({id}):"
		lookup_cache.insert(int(id), response.json())
		print('\nLookup Cache Obj:\nCache: ', lookup_cache.cache, '\nLRU_Queue: ', lookup_cache.lru_Q, '\n')
	else:
		msg = "Error! Cannot fetch book related to topic"
	
	return msg + '\n' + response.text, response.status_code, response.headers.items()

# Purchase query
@app.route('/purchase/<id>', methods=['PUT'])
def purchase(id):
	if not id.isnumeric():
		abort(422)
	# Call Order Server, get response
	order_ip, order_port = replication.get_order_info()
	response = requests.get(f'http://{order_ip}:{order_port}/purchase/{id}')
	
	msg = ""
	if response.status_code == 200:
		msg = "Book purchased successfully"
	else:
		msg = "Error! Cannot purchase"
	
	return msg + '\n' + response.text, response.status_code, response.headers.items()


# Update cost and quantity query
@app.route('/edit/<id>', methods=['PUT'])
def edit(id):
	if not id.isnumeric():
		abort(422)
	
	data = request.json

	if data is None:
		data = {}

	if data.get('quantity') is None or data.get('price') is None:
		abort(400)
	
	dataReq = {'quantity': data.get('quantity'), 'price': data.get('price')}
	# Call Catalog Server, get response
	response = requests.put(f'http://{replication.get_catalog_ip()}:{CATALOG_PORT[0]}/updateInfo/{id}', data=json.dumps(dataReq))
	
	msg = ""
	if response.status_code == 200:
		msg = "Updated Successfully"
	else:
		msg = "Error! Cannot update"
	
	return msg + '\n' + response.text, response.status_code, response.headers.items()
	

# ***********************************************************************************************
# Cache endpoints

# Route used by catalog servers to invalidate book entries
@app.route('/invalidate/item/<book_id>', methods=['DELETE'])
def invalidate_item(book_id):
    # If book is cached, remove it
    lookup_cache.remove(int(book_id))
    return 'Cache invalidated (id)', 204


# Route used by catalog servers to invalidate book topics
@app.route('/invalidate/topic/<book_topic>', methods=['DELETE'])
def invalidate_topic(book_topic):

    containing_entries = [key for key, value in search_cache.cache.items()
                          if book_topic in value.topics]

    # Remove any entry containing this topic
    for entry in containing_entries:
        search_cache.remove(entry)

    return 'Cache invalidated (topic)', 204



# Test endpoint that dumps all the cache contents
@app.route('/show-all-caches/', methods=['GET'])
def dump():
    response = {
        'lookup': [{'Tag': id, **lookup_cache.cache[id]} for id in lookup_cache.lru_Q],
        'search': [{'Tag': topic,
                    'topics': list(search_cache.cache[topic].topics),
                    'search_result': search_cache.cache[topic].search_result}
                    for topic in search_cache.lru_Q]
    }
    print(response)
    return response
