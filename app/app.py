from flask import Flask, jsonify
from pymongo import MongoClient
import os
import logging

app = Flask(__name__)

client = MongoClient(os.environ.get("MONGO_URI"))
db = client.get_database()

# Logging
if not os.path.exists('logs'):
    os.makedirs('logs')
logging.basicConfig(filename='logs/app.log', level=logging.INFO)

@app.route('/')
def index():
    logging.info("API accessed at / endpoint")
    return jsonify({"message": "Flask Mongo API Running Successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

