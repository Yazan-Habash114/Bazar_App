import requests

CATALOG_ADDRESSES = ['10.0.0.16', '10.0.0.9']
ORDER_ADDRESSES = ['10.0.0.11', '10.0.0.10']
FRONT_ADDRESS = '10.0.0.12'

CATALOG_PORTS = [5000, 5003]
ORDER_PORTS = [5001, 5004]
FRONT_PORT = 5002

def invalidate_item(book_id):
    response = requests.delete(f'http://{FRONT_ADDRESS}:{FRONT_PORT}/invalidate-item/{book_id}')

    msg = ""
    if response.status_code == 204:
    	msg = f"Book Invalidated (item/id)"
    else:
    	msg = "Error! Cannot invalidate proxy (cache)"
    
    return msg + '\n' + response.text, response.status_code, response.headers.items()


def invalidate_topic(book_topic):
    response = requests.delete(f'http://{FRONT_ADDRESS}:{FRONT_PORT}/invalidate-topic/{book_topic}')
    
    msg = ""
    if response.status_code == 204:
    	msg = f"Book Invalidated (topic)"
    else:
    	msg = "Error! Cannot invalidate proxy (cache)"
    
    return msg + '\n' + response.text, response.status_code, response.headers.items()
