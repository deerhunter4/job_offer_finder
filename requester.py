import requests

# For now request works only for default '24h' forecast period

# weatherapi.com API


def request_weatherapi(keys_dict, args):
    url_wheatherapi = 'https://api.weatherapi.com/v1/forecast.json'
    API_KEY_wheatherapi = keys_dict['wheatherapi.com']

    params_wheatherapi = dict(key=API_KEY_wheatherapi, q=args.location, days=1)
    resonse_wheatherapi = requests.get(url_wheatherapi, params=params_wheatherapi)

    # check if lack of proper request response is due to 403 error
    if resonse_wheatherapi.status_code == 403:
        print("Supplied API key for wheatherapi.com is wrong.")
        exit()

    resonse_wheatherapi_dict = resonse_wheatherapi.json()
    resonse_wheatherapi_hours = resonse_wheatherapi_dict['forecast']['forecastday'][0]['hour']

    # extracting needed information from request response
    hours_wheatherapi = []
    temp_c_wheatherapi = []
    rain_wheatherapi = []
    for item in resonse_wheatherapi_hours:
        hours_wheatherapi.append(item["time"])
        temp_c_wheatherapi.append(item["temp_c"])
        rain_wheatherapi.append(item['precip_mm'])

    # get latitute and longitute of the location
    latitude = resonse_wheatherapi_dict['location']['lat']
    longitude = resonse_wheatherapi_dict['location']['lon']

    weatherapi_dict = {'hours': hours_wheatherapi, 'temp': temp_c_wheatherapi,
                       'rain': rain_wheatherapi, 'latitude': latitude, 'longitude': longitude}

    return weatherapi_dict

# open-meteo.com API


def request_openmeteo(latitude, longitude):
    url_openmeteo = "https://api.open-meteo.com/v1/forecast"
    params_openmeteo = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": ["temperature_2m", "precipitation"],
        "forecast_days": 1
    }

    response_openmeteo = requests.get(url_openmeteo, params=params_openmeteo)
    response_openmeteo_dict = response_openmeteo.json()

    hours_openmeteo = response_openmeteo_dict['hourly']['time']
    temp_c_openmeteo = response_openmeteo_dict['hourly']['temperature_2m']
    rain_openmeteo = response_openmeteo_dict['hourly']['precipitation']

    openmeteo_dict = {'hours': hours_openmeteo, 'temp': temp_c_openmeteo,
                      'rain': rain_openmeteo, 'latitude': latitude, 'longitude': longitude}

    return openmeteo_dict

# meteostat.net


def request_meteostat(keys_dict, latitude, longitude, current_date):
    url_meteostat = 'https://meteostat.p.rapidapi.com/point/hourly'
    API_KEY_meteostat = keys_dict['meteostat.net']
    # current_date = hours_wheatherapi[1].split(' ')[0]

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

    response_meteostat = requests.get(url_meteostat, headers=headers_meteostat, params=params_meteostat)
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
