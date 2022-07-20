from flask import Flask, request, abort

app = Flask(__name__)

CATALOG_SERVER_IP = "172.16.102.196"
ORDER_SERVER_IP = "10.0.2.15"
CATALOG_PORT = 5000 
ORDER_PORT = 5001
