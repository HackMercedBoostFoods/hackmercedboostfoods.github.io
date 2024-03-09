from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import json

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))

analytics_data = json.load('collection.json')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)

class Analytics(db.Model):
    id = db.Column(db.String(200), primary_key=True,unique=True)
    rain = db.Column(db.Double)
    temp = db.Column(db.Double)
    crop_yied = db.Column(db.Double)

    def __init__(self):
        self.id = id
        self.rain = rain
        self.temp = temp
        self.crop_yield = crop_yield

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