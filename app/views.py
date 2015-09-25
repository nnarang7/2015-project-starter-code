from app import app, db, models
from flask import request, render_template
import json


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', coordinate_set = models.Coordinate.query.all())

@app.route('/health', methods=['GET'])
def health():
    print models.Coordinate.query.all()
    return "App is healthy", 200

@app.route('/coordinates', methods=['POST'])
def coordinates():
    r = request.json
    r_coordinates = r['coordinates']
    for item in r_coordinates:
        print item['latitude']
        print item['longitude']
        print item['notes']
        map_info = models.Coordinate(item['latitude'], item['longitude'], item['notes'])
        db.session.add(map_info)
        db.session.commit()
    
    
    return "testing"
