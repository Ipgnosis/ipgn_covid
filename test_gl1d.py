# test get_level1_data.py

from covid_package.api.get_country_data import get_country_data, get_level_1_data
from covid_package.libs.store_data import read_data
from covid_package.libs.valid_keys import fetch_l0_keys, fetch_l1_keys
import os
import sys

CURRENT_DIR = os.path.dirname(__file__)
sys.path.append(CURRENT_DIR)

COVID_PACKAGE = os.path.join(CURRENT_DIR, 'covid_package')
sys.path.append(COVID_PACKAGE)

FILE_NAME = 'owid-covid-data.json'
DATA_FILE = os.path.join(CURRENT_DIR, 'data', FILE_NAME)

# read the data file from the data dir
data = read_data(DATA_FILE)

# populate the level 0 key list excluding the aggregated records
key_list = fetch_l0_keys(data)

# generate the list of valid level 1 keys
l1_keys = fetch_l1_keys(data, key_list)

params = ['population', 'gdp_per_capita']

output = get_level_1_data(data, key_list, params)

print(output)
