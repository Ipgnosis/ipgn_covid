#  outputs list of distinct country key mappings

def get_country_key_mappings(this_data):

    keys_locations = this_data.items()

    return_str = {str(key): str(value["location"])
                  for key, value in keys_locations if str(key)[0:3] != "OWI"}

    return return_str


def main():
    from covid_package.libs.store_data import read_data

    # read the data file from the data dir
    data = read_data()

    # run the function
    print(get_country_key_mappings(data))


# stand alone test run
if __name__ == "__main__":
    main()
