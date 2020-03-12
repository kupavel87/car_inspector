from datetime import datetime
import json

from flask import Blueprint, flash, render_template, redirect, url_for, request, jsonify
from flask_login import current_user, login_user, logout_user
from sqlalchemy import extract

from webapp.db import db
from webapp.map.models import Car, Waybill

blueprint = Blueprint('map', __name__)


@blueprint.route("/")
def index():
    title = 'Карта передвижений'
    cars = Car.query.all()
    return render_template('map/index.html', page_title=title, cars=cars)


@blueprint.route("/get_dates", methods=['POST'])
def get_dates():
    plate = request.form['car']
    car = Car.query.filter_by(plate=plate).first()
    if car:
        date = request.form.get('date', '')
        if date:
            date = datetime.fromtimestamp(float(date) / 1000.0)
        else:
            date = datetime.today()
        dates = car.waybills.filter(extract('month', Waybill.timestamp) == date.month,
                                    extract('year', Waybill.timestamp) == date.year).all()

        dates = list(set([x.timestamp.strftime("%e").strip() for x in dates]))
        return jsonify({"dates": dates})


@blueprint.route("/get_route", methods=['POST'])
def get_route():
    plate = request.form['car']
    car = Car.query.filter_by(plate=plate).first()
    if car:
        date = request.form.get('date', '')
        if date:
            date = datetime.strptime(date, "%m/%d/%Y")
            route = car.waybills.filter(extract('day', Waybill.timestamp) == date.day, extract('month', Waybill.timestamp) == date.month,
                                        extract('year', Waybill.timestamp) == date.year).all()
            result = [[x.latitude, x.longitude] for x in route]
            return jsonify({"route": result})
