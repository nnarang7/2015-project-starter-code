from . import db
from datetime import datetime

class Coordinate(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    notes = db.Column(db.String(500))

    def __init__(self, latitude, longitude, notes):
        self.latitude = latitude
        self.longitude = longitude
        self.notes = notes

