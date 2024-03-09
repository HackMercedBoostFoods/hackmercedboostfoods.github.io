from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))

analytics_data = json.load('collection.json')

@app.route('/', methods=['GET'])
def home():
    return "Hello World!"

@app.route('/map', methods=['GET'])
def get_map():
    return "map"

@app.route('/map/<location>', methods=['POST'])
def post_map():
    return "map"

@app.route('/analytics/<user>', methods=['GET'])
def get_analytics():
    return jsonify(analytics_data)

@app.route('/analytics/{id}', methods=['POST'])
def post_analytics():
    return "analytics"

if __name__ == "__main__":
    app.run(debug=True)