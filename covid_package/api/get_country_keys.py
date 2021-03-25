#  outputs list of distinct country key mappings

def get_country_key_mappings(this_data):

    # return_str = "{"

    keys_locations = this_data.items()

    return_str = {str(key): str(value["location"])
                  for key, value in keys_locations if str(key)[0:3] != "OWI"}

    return return_str
