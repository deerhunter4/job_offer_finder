def parse_weatherapi_response(weatherapi_response):
    response_dict = weatherapi_response.json()
    forecast_hours = response_dict['forecast']['forecastday'][0]['hour']
    hours = []
    temp = []
    rain = []

    # extracting needed information from request response
    for item in forecast_hours:
        hours.append(item['time'])
        temp.append(item['temp_c'])
        rain.append(item['precip_mm'])

    latitude = response_dict['location']['lat']
    longitude = response_dict['location']['lon']

    return {'hours_weatherapi': hours, 'temp_weatherapi': temp,
            'rain_weatherapi': rain, 'latitude': latitude,
            'longitude': longitude}


def parse_openmeteo_response(response_openmeteo):
    response_dict = response_openmeteo.json()
    hours = response_dict['hourly']['time']
    temp = response_dict['hourly']['temperature_2m']
    rain = response_dict['hourly']['precipitation']
    latitude = response_dict['latitude']
    longitude = response_dict['longitude']

    return {'hours_openmeteo': hours, 'temp_openmeteo': temp,
            'rain_openmeteo': rain, 'latitude': latitude,
            'longitude': longitude}


def parse_meteostat_response(meteostat_response):
    response_dict = meteostat_response.json()
    hours = []
    temp = []
    rain = []

    for item in response_dict['data']:
        hours.append(item['time'])
        temp.append(item['temp'])
        rain.append(item['prcp'])

    return {'hours_meteostat': hours, 'temp_meteostat': temp,
            'rain_meteostat': rain}
