from flask_application import app 
from flask import request, abort
import requests
import json
import ast

CATALOG_SERVER_IP = '127.0.0.1'
PORT = 5000

@app.route('/purchase/<int:id>', methods=['GET'])
def purchase(id):
    response = requests.get(f'http://{CATALOG_SERVER_IP}:{PORT}/query-by-item/{id}')

    if(response.status_code == 200):
        response_json = response.json()
        quantity = response_json.get('quantity')
        price = response_json.get('price')
        # print("quantity ", quantity)
        # print("price ", price)
        message = ""
        if(quantity == 0):
            message = "There is no any more book to buy"

        else:
            data={'quantity': (quantity - 1), 'price': price}
            response = requests.put(f'http://{CATALOG_SERVER_IP}:{PORT}/update/{id}', data=json.dumps(data) )


    else: 
        abort(response.status_code)
        
    return response.text, response.status_code, response.headers.items()
        