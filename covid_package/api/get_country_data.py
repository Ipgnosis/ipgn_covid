#  outputs data for a country, based on a country key

import json


def get_country_data(this_data, this_country):

    country_data = json.dumps(
        this_data[this_country], indent=4, skipkeys=False)

    return country_data

