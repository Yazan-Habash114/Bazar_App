from flask_application import app, CATALOG_SERVER_IP, ORDER_SERVER_IP, PORT, abort
import requests


# Search query
@app.route('/search/<topic>', methods=['GET'])
def search_according_to_topic(topic):
	response = requests.get(f'http://{CATALOG_SERVER_IP}:{PORT}/query-by-subject/{topic}')
	
	return response.text, response.status_code, response.headers.items()


# Info query
@app.route('/info/<id>', methods=['GET'])
def info_according_to_id(id):
	if not id.isnumeric():
		abort(422)
	
	response = requests.get(f'http://{CATALOG_SERVER_IP}:{PORT}/query-by-item/{id}')
	
	return response.text, response.status_code, response.headers.items()
