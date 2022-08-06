from flask import Flask, request, abort

app = Flask(__name__)

CATALOG_SERVER_IP = "10.0.0.9"
ORDER_SERVER_IP = "10.0.0.10"
CATALOG_PORT = 5000 
ORDER_PORT = 5001
