
# pip install requests

import requests
import json
import os

keys_path = './better_weather_keys.txt'

# Check if better_weather_keys.txt file exists and it is not empty
if os.path.isfile(keys_path) and os.stat(keys_path).st_size != 0:
    keys_file = open(keys_path, "r")
else:
    print("Warning: File better_weather_keys.txt is not in the working directory or it is empty!")

# read input file as list dictionary
keys_dict = {}
for line in keys_file:
    key, value = line.strip().split(',')
    keys_dict[key] = value

keys_file.close()

######################
### weatherapi.com ###
######################

# You need to register on the web page first to get API key
# https://www.weatherapi.com/signup.aspx
# The url is set to get forecast data. For historical data it should be changed

# KeyError exception handling
url_wheatherapi = 'https://api.weatherapi.com/v1/forecast.json'
try:
    API_KEY_wheatherapi = keys_dict['wheatherapi.com']
except KeyError:
    print("The key name in the file better_weather_keys.txt is incorrect, should be 'wheatherapi.com'")

# You can change the name of the city <q parameter>, search engine is quite efficient
# days=1 means that you get hourly forecast for one date, the day you are make a request. 
# To get forecast for next day you need additional parameter
params_wheatherapi = dict(key=API_KEY_wheatherapi, q='Przemysl', days=1) 

resonse_wheatherapi = requests.get(url_wheatherapi, params=params_wheatherapi)

# check if lack of proper request response is due to 403 error
if resonse_wheatherapi.status_code == 403:
    print("Supplied API key for wheatherapi.com is wrong.")

# print(resonse_wheatherapi)
# print(resonse_wheatherapi.status_code)
# print(resonse_wheatherapi.headers)
# print(resonse_wheatherapi.json())

# text = json.dumps(resonse_wheatherapi.json(), sort_keys=True, indent=4)
# print(text)

resonse_wheatherapi_dict = resonse_wheatherapi.json()
# resonse_wheatherapi_dict.keys()
# rresonse_wheatherapi_forecast = resonse_wheatherap_dict['forecast']
# resonse_wheatherapi_forecast.keys()
# resonse_wheatherapi_forecastday = resonse_wheatherap_forecast['forecastday']

resonse_wheatherapi_hours = resonse_wheatherapi_dict['forecast']['forecastday'][0]['hour']
# res_hours[4]

hours_wheatherapi = []
temp_c_wheatherapi = []
rain_wheatherapi = []
for item in resonse_wheatherapi_hours:
    hours_wheatherapi.append(item["time"])
    temp_c_wheatherapi.append(item["temp_c"])
    rain_wheatherapi.append(item['precip_mm'])

print(hours_wheatherapi)
print(temp_c_wheatherapi)
print(rain_wheatherapi)

######################
### open-meteo.com ###
######################

# for using this webpage API you do not need API key
# to request you need to give latitute and longitute of the location,
# however we can get this data from request above, because we get this info as an output

latitude = resonse_wheatherapi_dict['location']['lat']
longitude = resonse_wheatherapi_dict['location']['lon']

url_openmeteo = "https://api.open-meteo.com/v1/forecast"
params_openmeteo = {
	"latitude": latitude,
	"longitude": longitude,
	"hourly": ["temperature_2m", "precipitation"],  # here we can extend number of parameters
	"forecast_days": 1
}

response_openmeteo = requests.get(url_openmeteo, params=params_openmeteo)
response_openmeteo_dict = response_openmeteo.json()

hours_openmeteo = response_openmeteo_dict['hourly']['time']
temp_c_openmeteo = response_openmeteo_dict['hourly']['temperature_2m']
rain_openmeteo = response_openmeteo_dict['hourly']['precipitation']

# below you can compare forecasts from bothe webpages, and yes, they differ :)

print(hours_openmeteo)
print(temp_c_openmeteo)
print(rain_openmeteo)

print(hours_wheatherapi)
print(hours_openmeteo)

print(temp_c_wheatherapi)
print(temp_c_openmeteo)


#####################
### meteostat.net ###
#####################

# You need to register on the web page first to get API key
# https://rapidapi.com/meteostat/api/meteostat/pricing
# The url is set to get forecast data. For historical data it should be changed

url_meteostat = 'https://meteostat.p.rapidapi.com/point/hourly'
API_KEY_meteostat = keys_dict['meteostat.net']
current_date = hours_wheatherapi[1].split(' ')[0]

params_meteostat = {
	"lat": latitude,
	"lon": longitude,
	"start": current_date, # current day obtained from first api request
	"end": current_date
}

headers_meteostat = {
	"X-RapidAPI-Key": API_KEY_meteostat,
	"X-RapidAPI-Host": "meteostat.p.rapidapi.com"
}

response_meteostat = requests.get(url_meteostat, headers=headers_meteostat, params=params_meteostat)
response_meteostat_dict = response_meteostat.json()

hours_meteostat = []
temp_c_meteostat = []
rain_meteostat = []
for item in response_meteostat_dict["data"]:
    hours_meteostat.append(item['time'])
    temp_c_meteostat.append(item['temp'])
    rain_meteostat.append(item['prcp'])

print(hours_meteostat)
print(temp_c_meteostat)
print(rain_meteostat)

print('', temp_c_wheatherapi, '\n',temp_c_openmeteo, '\n', temp_c_meteostat)

print('', rain_wheatherapi, '\n', rain_openmeteo, '\n', rain_meteostat)

print('', hours_wheatherapi[1], '\n', hours_openmeteo[1], '\n', hours_meteostat[1]) # three different time formats
