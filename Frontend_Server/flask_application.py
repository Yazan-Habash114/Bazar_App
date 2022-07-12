from flask import Flask, request, abort

app = Flask(__name__)

CATALOG_SERVER_IP = "127.0.0.1"
ORDER_SERVER_IP = "127.0.0.1"
CATALOG_PORT = 5000 
ORDER_PORT = 66

