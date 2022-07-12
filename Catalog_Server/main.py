from database import create_db
create_db()

from routes import *

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=5000)
