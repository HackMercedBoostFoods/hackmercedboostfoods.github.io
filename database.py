from flask import Flask, render_template, request
import subprocess as sp
from pymongo import MongoClient

from mongopass import mongopass

app = Flask("HackMerced")

client = MongoClient(mongopass)

#did not autofill
db = client.curd
myCollection = db.myColl

@app.route('/')

def home():
    return 'Hello, World!'
