from flask import Blueprint, abort, jsonify, request
from google.cloud import ndb
from shared.model.car import Car
from shared.model.garage import Garage
import logging

bp = Blueprint(name='cars', import_name=__name__, url_prefix='/<garage_id>/cars')

# @garages.route('/', defaults={'page': 'index'})
@bp.route('/', methods=["GET"])
def car_list(garage_id):
    print(garage_id)
    garage = Garage.get(int(garage_id))
    if garage:
        if request.args and 'car' in request.args:
            car = Car.get(key=request.args.get('car'), parent=garage.key)
            return jsonify(car_to_json(car))
        return jsonify(
            [
                car_to_json(car) for car in Car.list(garage=garage)
            ]
        )
    return jsonify({
        'message': 'not found'
    }), 404


@bp.route('/', methods=["POST"])
def car_add(garage_id):
    garage = Garage.get(garage_id)
    logging.warning(request.json)
    car = Car.add(props=request.json, parent=garage.key)
    return jsonify(car_to_json(car))

@bp.route('/', methods=["PUT"])
def car_update(garage_id):
    props = request.json
    garage = Garage.get(garage_id)
    car = Car.get(key=props.pop('id'), parent=garage.key)
    # print(garage)
    car.update(props=props)
    return jsonify(car_to_json(car))

@bp.route('/', methods=["DELETE"])
def car_delete(garage_id):
    garage = Garage.get(key=garage_id)
    car = Car.get(key=request.json.pop('id'), parent=garage.key)
    car.delete()
    return jsonify({'status': 'OK'})


def car_to_json(car):
    return {
        'id': car.id,
        'name': car.name,
        'brand': car.brand,
        'color': car.color,
        'license_plate': car.license_plate
    }