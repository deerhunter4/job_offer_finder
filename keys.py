import os


# read input file as a dictionary
def read_keys(keys_file):
    keys_dict = {}
    for line in keys_file:
        key, value = line.strip().split(',')
        keys_dict[key] = value

    keys_file.close()

    if 'weatherapi.com' not in keys_dict or 'meteostat.net' not in keys_dict:
        print("""The keys are missing in the better_weather_keys.txt file
                or their names might be incorrect. The correct names are:
                'weatherapi.com', 'meteostat.net'""")
        exit()

    return keys_dict


def check_keys(keys_path):
    # Check if better_weather_keys.txt file exists and it is not empty
    if os.path.isfile(keys_path) and os.stat(keys_path).st_size != 0:
        keys_file = open(keys_path, "r")
        return read_keys(keys_file)
    else:
        print("""Error: File better_weather_keys.txt is not in
            the working directory or it is empty!""")
        exit()
