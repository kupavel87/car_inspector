from datetime import datetime

from webapp.db import db


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(9), unique=True)
    description = db.Column(db.String(255))
    waybills = db.relationship('Waybill', backref='car', lazy='dynamic')

    def __repr__(self):
        return '<Машина {}>'.format(self.plate)


class Waybill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Машина {}, дата {}>'.format(self.car_id.plate, self.timestamp)
