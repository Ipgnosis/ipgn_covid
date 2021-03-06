# modules to check for expiry, read, download/write and delete covid data

import json


def read_data(fname):

    with open(fname) as json_file:
        data = json.load(json_file)

    return data
