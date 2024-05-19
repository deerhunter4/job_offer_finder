import os

KEYS_PATH = './better_weather_keys.txt'


# read input file as a dictionary
def read_keys(keys_file):
    keys_dict = {}
    for line in keys_file:
        key, value = line.strip().split(',')
        keys_dict[key] = value

    keys_file.close()

    if 'weatherapi.com' not in keys_dict or 'meteostat.net' not in keys_dict:
        print("""KeyError: The API key names in the better_weather_keys.txt
              file are missing or their names might be incorrect.
              The correct names are: 'weatherapi.com', 'meteostat.net'""")
        exit()

    return keys_dict


# Check if better_weather_keys.txt file exists and it is not empty
def check_keys():
    if os.path.isfile(KEYS_PATH) and os.stat(KEYS_PATH).st_size != 0:
        keys_file = open(KEYS_PATH, "r")
        return read_keys(keys_file)
    else:
        print("""KeyError: File better_weather_keys.txt is not in
            the working directory or it is empty!""")
        exit()
