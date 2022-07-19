from flask_application import app, CATALOG_SERVER_IP, ORDER_SERVER_IP, ORDER_PORT, CATALOG_PORT, abort
import requests


# Search query
@app.route('/search/<topic>', methods=['GET'])
def search_according_to_topic(topic):
	# Call Catalog Server, get response
	response = requests.get(f'http://{CATALOG_SERVER_IP}:{CATALOG_PORT}/query-by-subject/{topic}')
	
	return response.text, response.status_code, response.headers.items()


# Info query
@app.route('/info/<id>', methods=['GET'])
def info_according_to_id(id):
	if not id.isnumeric():
		abort(422)
	# Call Catalog Server, get response
	response = requests.get(f'http://{CATALOG_SERVER_IP}:{CATALOG_PORT}/query-by-item/{id}')
	
	return response.text, response.status_code, response.headers.items()

# Info query
@app.route('/purchase/<id>', methods=['PUT'])
def purchase(id):
	if not id.isnumeric():
		abort(422)
	# Call Catalog Server, get response
	response = requests.get(f'http://{ORDER_SERVER_IP}:{ORDER_PORT}/purchase/{id}')
	
	return response.text, response.status_code, response.headers.items()



