# build a table of the iso_code, continent, location
# created by Russell on 3/25/21

from covid_package.api.get_country_data import get_level_1_data
from covid_package.libs.store_data import read_data
from covid_package.libs.valid_keys import fetch_l0_keys
import os
import sys

CURRENT_DIR = os.path.dirname(__file__)
sys.path.append(CURRENT_DIR)

FILE_NAME = 'owid-covid-data.json'
DATA_FILE = os.path.join(CURRENT_DIR, 'data', FILE_NAME)

# read the data file from the data dir
data = read_data(DATA_FILE)

"""
def get_level_1_data(this_data, these_keys, req_keys):

    return_dict = dict()

    for iso in these_keys:
        country_dict = dict()
        for req_key in req_keys:
            if req_key in this_data[iso].keys():
                country_dict[req_key] = this_data[iso][req_key]
        return_dict[iso] = country_dict

    return return_dict
"""

# populate the level 0 key list excluding the aggregated records
iso_list = fetch_l0_keys(data)

rows = get_level_1_data(data, iso_list, ['continent', 'location'])

table_header = "<table>\n<tr>\n<th>iso_code</th>\n<th>continent</th>\n<th>location</th>\n</tr>\n"

table_footer = "</table>"
#table_list = list

print(table_header)

# for row in rows:
