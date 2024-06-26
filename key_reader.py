import os

KEYS_PATH = './better_weather_keys.txt'


# read input file as a dictionary
def read_keys():
    keys_dict = {}
    keys_file = open(KEYS_PATH, "r")
    try:
        for line in keys_file:
            key, value = line.strip().split(',')
            keys_dict[key] = value
    except ValueError:
        raise ValueError(f"File {KEYS_PATH} has an incorrect format.\n"
                         "It should be a comma-delimited text, "
                         "following the scheme:"
                         "\"<key-name>,<key-value>\"")

    keys_file.close()

    if 'weatherapi.com' not in keys_dict or 'meteostat.net' not in keys_dict:
        raise KeyError("The API key names in the better_weather_keys.txt "
                       "file are missing or their names might be incorrect. "
                       "The correct names are: 'weatherapi.com', 'meteostat.net'")

    return keys_dict


# Check if better_weather_keys.txt file exists and it is not empty
def get_keys():
    if os.path.isfile(KEYS_PATH) and os.stat(KEYS_PATH).st_size != 0:
        return read_keys()
    else:
        raise FileNotFoundError(f"File {KEYS_PATH} is not in "
                                "the working directory or it is empty!")
