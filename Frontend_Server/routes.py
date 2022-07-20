from flask_application import app, CATALOG_SERVER_IP, ORDER_SERVER_IP, ORDER_PORT, CATALOG_PORT, abort, request
import requests
import json


# Search query
@app.route('/search/<topic>', methods=['GET'])
def search_according_to_topic(topic):
	# Call Catalog Server, get response
	response = requests.get(f'http://{CATALOG_SERVER_IP}:{CATALOG_PORT}/query-by-subject/{topic}')
	
	msg = ""
	if response.status_code == 200:
		msg = "Book with ID:"
	else:
		msg = "Error! Cannot fetch book with ID"
		
	return response.text, response.status_code, response.headers.items()


# Info query
@app.route('/info/<id>', methods=['GET'])
def info_according_to_id(id):
	if not id.isnumeric():
		abort(422)
	# Call Catalog Server, get response
	response = requests.get(f'http://{CATALOG_SERVER_IP}:{CATALOG_PORT}/query-by-item/{id}')
	
	msg = ""
	if response.status_code == 200:
		msg = "All books related to topic:"
	else:
		msg = "Error! Cannot fetch book related to topic"
	
	return msg + '\n' + response.text, response.status_code, response.headers.items()

# Purchase query
@app.route('/purchase/<id>', methods=['PUT'])
def purchase(id):
	if not id.isnumeric():
		abort(422)
	# Call Order Server, get response
	response = requests.get(f'http://{ORDER_SERVER_IP}:{ORDER_PORT}/purchase/{id}')
	
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
	response = requests.put(f'http://{CATALOG_SERVER_IP}:{CATALOG_PORT}/updateInfo/{id}', data=json.dumps(dataReq))
	
	msg = ""
	if response.status_code == 200:
		msg = "Updated Successfully"
	else:
		msg = "Error! Cannot update"
	
	return msg + '\n' + response.text, response.status_code, response.headers.items()
