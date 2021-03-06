# app.py to run covid API
# created by Russell on 3/6/21

from covid_package.api.get_country_data import get_country_data
from covid_package.api.get_country_keys import get_country_key_mappings
from covid_package.api.home import home_screen
from covid_package.libs.country_list import fetch_keys
from covid_package.libs.store_data import read_data
import os
import sys
from flask import Flask, request

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

# populate the key list and country list excluding the aggregated records
key_list = fetch_keys(data)

# API

# the default route


@app.route('/')
def default_route():
    # return package.get_country_records(data, key_list)
    return home_screen()

# the country api


@app.route('/country')
def country_route():

    iso_code = request.args.get('iso')

    if iso_code in key_list:
        return get_country_data(data, iso_code)
    else:
        return get_country_key_mappings(data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
