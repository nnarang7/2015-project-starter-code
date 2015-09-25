from app import app, db, models
from flask import request
import json


@app.route('/', methods=['GET'])
def index():
    return 'Hello world!'

@app.route('/health', methods=['GET'])
def health():
    return "App is healthy!", 200

@app.route('/coordinates', methods=['POST'])
def coordinates():
    r = request.data
    r_json1 = json.dumps(r)
    r_json2 = json.loads(r_json1)
    for key, value in r_json2:
	print key
	print value
    return "testing"
