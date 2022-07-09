from flask import Flask, request, abort

app = Flask(__name__)

CATALOG_SERVER_IP = "10.0.0.14"
ORDER_SERVER_IP = "10.0.0.16"
PORT = 5000
