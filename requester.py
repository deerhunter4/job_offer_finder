import requests

URL_WEATHERAPI = 'https://api.weatherapi.com/v1/forecast.json'
URL_OPENMETEO = "https://api.open-meteo.com/v1/forecast"
URL_METEOSTAT = 'https://meteostat.p.rapidapi.com/point/hourly'

# Note: For now all requests work only for the default '24h' forecast period.

# weatherapi.com API


def request_weatherapi(keys_dict, args):
    API_KEY_weatherapi = keys_dict['weatherapi.com']

    params_weatherapi = dict(key=API_KEY_weatherapi, q=args.location, days=1)
    resonse_weatherapi = requests.get(URL_WEATHERAPI, params=params_weatherapi)

    # check if lack of proper request response is due to 403 error
    if resonse_weatherapi.status_code == 403:
        print("Supplied API key for weatherapi.com is wrong.")
        exit()

    resonse_weatherapi_dict = resonse_weatherapi.json()
    resonse_weatherapi_hours = resonse_weatherapi_dict['forecast']['forecastday'][0]['hour']

    # extracting needed information from request response
    hours_weatherapi = []
    temp_c_weatherapi = []
    rain_weatherapi = []
    for item in resonse_weatherapi_hours:
        hours_weatherapi.append(item["time"])
        temp_c_weatherapi.append(item["temp_c"])
        rain_weatherapi.append(item['precip_mm'])

    # get latitute and longitute of the location
    latitude = resonse_weatherapi_dict['location']['lat']
    longitude = resonse_weatherapi_dict['location']['lon']

    weatherapi_dict = {'hours': hours_weatherapi, 'temp': temp_c_weatherapi,
                       'rain': rain_weatherapi, 'latitude': latitude, 'longitude': longitude}

    return weatherapi_dict, latitude, longitude

# open-meteo.com API


def request_openmeteo(latitude, longitude):
    params_openmeteo = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": ["temperature_2m", "precipitation"],
        "forecast_days": 1
    }

    response_openmeteo = requests.get(URL_OPENMETEO, params=params_openmeteo)
    response_openmeteo_dict = response_openmeteo.json()

    hours_openmeteo = response_openmeteo_dict['hourly']['time']
    temp_c_openmeteo = response_openmeteo_dict['hourly']['temperature_2m']
    rain_openmeteo = response_openmeteo_dict['hourly']['precipitation']

    openmeteo_dict = {'hours': hours_openmeteo, 'temp': temp_c_openmeteo,
                      'rain': rain_openmeteo, 'latitude': latitude, 'longitude': longitude}

    return openmeteo_dict

# meteostat.net


def request_meteostat(keys_dict, latitude, longitude, current_date):
    API_KEY_meteostat = keys_dict['meteostat.net']

    params_meteostat = {
        "lat": latitude,
        "lon": longitude,
        "start": current_date,  # current day obtained from first api request
        "end": current_date
    }

    headers_meteostat = {
        "X-RapidAPI-Key": API_KEY_meteostat,
        "X-RapidAPI-Host": "meteostat.p.rapidapi.com"
    }

    response_meteostat = requests.get(URL_METEOSTAT, headers=headers_meteostat, params=params_meteostat)
    response_meteostat_dict = response_meteostat.json()

    hours_meteostat = []
    temp_c_meteostat = []
    rain_meteostat = []
    for item in response_meteostat_dict["data"]:
        hours_meteostat.append(item['time'])
        temp_c_meteostat.append(item['temp'])
        rain_meteostat.append(item['prcp'])

    meteostat_dict = {'hours': hours_meteostat, 'temp': temp_c_meteostat,
                      'rain': rain_meteostat, 'latitude': latitude, 'longitude': longitude}

    return meteostat_dict
