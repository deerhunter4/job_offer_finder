
# pip install requests

import requests
import json

######################
### weatherapi.com ###
######################

# You need to register on the web page first to get API key
# https://www.weatherapi.com/signup.aspx
# The url is set to get forecast data. For historical data it should be changed

url = 'https://api.weatherapi.com/v1/forecast.json'
API_KEY = <paste here your personal API key>

# You can change the name of the city <q parameter>, search engine is quite efficient
# days=1 means that you get hourly forecast for one date, the day you are make a request. 
# To get forecast for next day you need additional parameter
params = dict(key=API_KEY, q='Przemysl', days=1) 

res = requests.get(url, params=params)

# print(res)
# print(res.status_code)
# print(res.headers)
# print(res.json())

# text = json.dumps(res.json(), sort_keys=True, indent=4)
# print(text)

res_dict = res.json()
# res_dict.keys()
# res_forecast = res_dict['forecast']
# res_forecast.keys()
# res_forecastday = res_forecast['forecastday']

res_hours = res_dict['forecast']['forecastday'][0]['hour']
# res_hours[4]

hours = []
temp_c = []
rain = []
for item in res_hours:
    hours.append(item["time"])
    temp_c.append(item["temp_c"])
    rain.append(item['precip_mm'])

print(hours)
print(temp_c)
print(rain)

######################
### open-meteo.com ###
######################

# for using this webpage API you do not need API key
# to request you need to give latitute and longitute of the location,
# however we can get this data from request above, because we get this info as an output

lat = res_dict['location']['lat']
lon = res_dict['location']['lon']

url_2 = "https://api.open-meteo.com/v1/forecast"
params_2 = {
	"latitude": lat,
	"longitude": lon,
	"hourly": ["temperature_2m", "precipitation"], # here we can extend number of parameters
	"forecast_days": 1
}

res_2 = requests.get(url_2, params=params_2)
res_2_dict = res_2.json()

hours_2 = res_2_dict['hourly']['time']
temp_c_2 = res_2_dict['hourly']['temperature_2m']
rain_2 = res_2_dict['hourly']['precipitation']

# below you can compare forecasts from bothe webpages, and yes, they differ :)

print(hours_2)
print(temp_c_2)
print(rain_2)

print(hours)
print(hours_2)

print(temp_c)
print(temp_c_2)


#####################
### meteostat.net ###
#####################

# You need to register on the web page first to get API key
# https://rapidapi.com/meteostat/api/meteostat/pricing
# The url is set to get forecast data. For historical data it should be changed

url_3 = 'https://meteostat.p.rapidapi.com/point/hourly'
API_KEY_3 = <paste here your personal API key>

params_3 = {
	"lat": lat,
	"lon": lon,
	"start":"2024-02-28", #here we have to use some timestump to do it automaticaly
    "end":"2024-02-28"
}

headers_3 = {
	"X-RapidAPI-Key": <paste here your personal API key>,
	"X-RapidAPI-Host": "meteostat.p.rapidapi.com"
}

res_3 = requests.get(url_3, headers= headers_3, params= params_3)
res_3_dict = res_3.json()

hours_3 = []
temp_c_3 = []
rain_3 = []
for item in res_3_dict["data"]:
    hours_3.append(item['time'])
    temp_c_3.append(item['temp'])
    rain_3.append(item['prcp'])
    
print(hours_3)
print(temp_c_3)
print(rain_3)

print(temp_c), print(temp_c_2), print(temp_c_3)

print(rain), print(rain_2), print(rain_3)

print(hours[1]), print(hours_2[1]), print(hours_3[1]) # three different time formats