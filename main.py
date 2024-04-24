from datetime import date
from arguments import parameters
from keys import check_keys
from requester import request_weatherapi, request_openmeteo, request_meteostat

KEYS_PATH = './better_weather_keys.txt'

# get current date
current_date = str(date.today())
print(current_date)

# get parameters that will be used by the requester component
parameters = parameters()
print(parameters)

# get API keys from the file
keys = check_keys(KEYS_PATH)
print(f"The API keys have correct names:\n{list(keys.keys())}")

# request to wheatherapi; get latitude and longitude of the location
weatherapi_forecast, latitude, longitude = request_weatherapi(keys, parameters)
print(weatherapi_forecast)

# request to wheatherapi
openmeteo_forecast = request_openmeteo(latitude, longitude)
print(openmeteo_forecast)

# request to meteostat
meteostat_forecast = request_meteostat(keys, latitude, longitude, current_date)
print(meteostat_forecast)


if __name__ == "__main__":
    print("Enjoy the weather forecast.")
