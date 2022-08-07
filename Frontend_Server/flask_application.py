from flask import Flask, request, abort

app = Flask(__name__)

CATALOG_SERVER_IP = ["10.0.0.16", "10.0.0.1"]
ORDER_SERVER_IP = ["10.0.0.10", "10.0.0.14"]
CATALOG_PORT = [5000, 5003] 
ORDER_PORT = [5001, 5004]
