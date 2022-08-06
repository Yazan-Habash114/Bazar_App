from flask_application import app

# Here we will handle the happened errors when calling APIs

@app.errorhandler(500)
def internal_server_error(err):
	return 'The server has encountered an internal error and was unable to complete your request.', 500
	

@app.errorhandler(404)
def not_found(err):
	return 'The request URL was not found on this server.', 404
	

@app.errorhandler(400)
def bad_request(err):
	return 'Bad request, the URL isn\'t supplied.', 400
	
	
@app.errorhandler(405)
def method_not_allowed(err):
	return 'This method is not allowed for the requeted URL.', 405
	

@app.errorhandler(422)
def unprocessable_entity(err):
	return 'Unprocessable entity: the value must be numeric.', 422
