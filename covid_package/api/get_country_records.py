# output key information on available data by country

from covid_package.libs.aggregate_data import count_daily_records, fetch_date_range


def get_country_records(this_data, list_of_keys):

    return_str = str

    for iso in list_of_keys:

        this_country = this_data[iso]["location"]
        daily_records = count_daily_records(this_data, iso)
        date_range = fetch_date_range(this_data, iso)
        iso_str = "\n{}: {} = {}; from {} to {}.".format(
            iso, this_country, daily_records, date_range[0], date_range[1])
        return_str += iso_str

    return return_str


def main():

    import sys

    sys.path.append("c:\\Users\\Ipgnosis\\Documents\\Github\\ipgn_covid")

    from covid_package.libs.store_data import read_data
    from covid_package.libs.country_list import fetch_keys

    # read the data file from the data dir
    data = read_data()

    key_list = fetch_keys(data)

    # run the function
    print(get_country_records(data, key_list))


# stand alone test run
if __name__ == "__main__":
    main()
