from flask_application import app 
from flask import request, abort
import requests
import json
import ast

CATALOG_SERVER_IP = '10.0.0.9'
PORT = 5003

@app.route('/purchase/<int:id>', methods=['GET'])
def purchase(id):
    # Call Catalog Server, get response
    response = requests.get(f'http://{CATALOG_SERVER_IP}:{PORT}/query-by-item/{id}')
    
    # If the status of response is OK
    if(response.status_code == 200):
        response_json = response.json()
        quantity = response_json.get('quantity')
        price = response_json.get('price')
        # print("quantity ", quantity)
        # print("price ", price)
        message = ""
        # If the stock is empty
        if(quantity == 0):
            message = "There is no any more book to buy"
            return message, response.status_code, response.headers.items()

        else:
            # Else, return the book, decrement the quantity
            data = {'quantity': (quantity - 1), 'price': price}
            response = requests.put(f'http://{CATALOG_SERVER_IP}:{PORT}/update/{id}', data=json.dumps(data))


    else: 
        message = "This book is not found!"
        return message, response.status_code, response.headers.items()
        
    return response.text, response.status_code, response.headers.items()
        
