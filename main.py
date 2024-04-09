from arguments import parameters
from keys import check_keys
from requester import request_weatherapi, request_openmeteo, request_meteostat

# get parameters
param = parameters()
print(param)

# get API keys from the file
keys = check_keys()
print(f"The API keys have correct names:\n{list(keys.keys())}")

# request to wheatherapi
weatherapi_forecast = request_weatherapi(keys, param)
print(weatherapi_forecast)
latitude = weatherapi_forecast['latitude']
longitude = weatherapi_forecast['longitude']
current_date = weatherapi_forecast['hours'][1].split(' ')[0]

# request to wheatherapi
openmeteo_forecast = request_openmeteo(latitude, longitude)
print(openmeteo_forecast)

# request to meteostat
meteostat_forecast = request_meteostat(keys, latitude, longitude, current_date)
print(meteostat_forecast)


# if __name__ == "__main__":
#     main()
