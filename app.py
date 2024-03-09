from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))

analytics_data = json.load('collection.json')

maps_api_key = 'AIzaSyDyw8uZxBN17mPkDiobQaZyB0kQcJgg8M0'
maps_embed_api = 'AIzaSyAaOICRptEhBPObpkgZ9U9tOZJUppxlbYA'

@app.route('/', methods=['GET'])
def home():
    return "Hello World!"

@app.route('/map', methods=['GET'])
def get_map():
    return 

@app.route('/map/<location>', methods=['POST'])
def post_map():
    return "map"

@app.route('/analytics/', methods=['GET'])
def get_analytics():
    return jsonify(analytics_data)

@app.route('/analytics/<user>', methods=['POST'])
def post_analytics():
    return "analytics"

if __name__ == "__main__":
    app.run(debug=True)