# app.py to run covid API
# created by Russell on 3/6/21

from covid_package.api.get_latest_date import get_latest_date
from covid_package.api.get_country_data import get_country_data, get_level_1_data, get_l2_keys_data
from covid_package.api.home import home_screen
from covid_package.libs.store_data import read_data
from covid_package.libs.valid_keys import fetch_l0_keys, fetch_l1_keys, fetch_l2_keys, valid_fields
from covid_package.classes.Exception_class import InvalidUsage
import os
import sys
from flask import Flask, request, jsonify
from flask_swagger import swagger

CURRENT_DIR = os.path.dirname(__file__)
sys.path.append(CURRENT_DIR)

COVID_PACKAGE = os.path.join(CURRENT_DIR, 'covid_package')
sys.path.append(COVID_PACKAGE)

FILE_NAME = 'owid-covid-data.json'
DATA_FILE = os.path.join(CURRENT_DIR, 'data', FILE_NAME)

# create the Flask app
app = Flask(__name__)

# read the data file from the data dir
data = read_data(DATA_FILE)

# populate the level 0 key list excluding the aggregated records
iso_list = fetch_l0_keys(data)

# generate the list of valid level 1 keys
l1_keys = fetch_l1_keys(data, iso_list)

# generate the list of valid level 2 keys
l2_keys = fetch_l2_keys(data, iso_list)

# API

# the default route


@app.route('/')
def default_route():
    # return package.get_country_records(data, key_list)
    return home_screen()


# register the error handler


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


# the swagger doc route


@app.route('/spec')
def spec():
    return jsonify(swagger(app))


# the country api


@app.route('/country')
def country_route():

    if request.args.get('iso'):
        iso_code = request.args.get('iso')
    else:
        raise InvalidUsage(
            'This resource does not exist - check documentation', status_code=404)

    if iso_code in iso_list:
        return get_country_data(data, iso_code)
    else:
        raise InvalidUsage(
            'This iso_code does not exist - check documentation', status_code=404)


# the level 1 api
# NOTE THAT level 1 data does NOT include the key 'data'
# the key 'data' is deemed to be the key for level 2 data


@app.route('/level1')
def level_1_route():

    if request.args.get('keys'):
        req_keys_list = request.args.get('keys').split(',')
    else:
        raise InvalidUsage(
            'This resource does not exist - check documentation', status_code=404)

    if valid_fields(req_keys_list, l1_keys):
        return get_level_1_data(data, iso_list, req_keys_list)
    else:
        raise InvalidUsage(
            'One or more parameters do not exist - check documentation', status_code=404)


# the level 2 api


@app.route('/level2')
# split out the key and the data api
def level_2_route():

    if request.args.get('keys'):
        req_keys_list = request.args.get('keys').split(',')
    else:
        raise InvalidUsage(
            'This resource does not exist - check documentation', status_code=404)

    if valid_fields(req_keys_list, l2_keys):
        return get_l2_keys_data(data, iso_list, req_keys_list)
    else:
        raise InvalidUsage(
            'One or more parameters do not exist - check documentation', status_code=404)


# poll for latest data to validate data update service


@app.route('/latest_data')
def date_check_route():
    # return package.get_country_records(data, key_list)
    return get_latest_date(data, iso_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
