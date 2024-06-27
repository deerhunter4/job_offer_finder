import requests
from response_parser import parse_weatherapi_response, parse_meteostat_response, parse_openmeteo_response

URL_WEATHERAPI = 'https://api.weatherapi.com/v1/forecast.json'
URL_OPENMETEO = 'https://api.open-meteo.com/v1/forecast'
URL_METEOSTAT = 'https://meteostat.p.rapidapi.com/point/hourly'
WEATHERAPI_NAME = 'weatherapi.com'
OPENMETEO_NAME = 'open-meteo.com'
METEOSTAT_NAME = 'meteostat.net'

# Note: For now all requests work only for the default '24h' forecast period.


# check for the 403 and 503 error
def response_errors(api_response, name):
    if api_response.status_code == 403:
        raise KeyError(f"The API key provided for {name} is invalid.")
    elif api_response.status_code == 503:
        raise ConnectionError(f"ServiceError: {name} server is down for "
                              "maintenance or is overloaded. Try again in "
                              "a few minutes.")


# weatherapi.com API
def request_weatherapi(api_key, args):
    weatherapi_params = dict(key=api_key, q=args.location, days=1)
    weatherapi_response = requests.get(URL_WEATHERAPI, params=weatherapi_params)

    # check if lack of proper request response is due to 403 or 503 error
    response_errors(weatherapi_response, WEATHERAPI_NAME)

    return parse_weatherapi_response(weatherapi_response)


# open-meteo.com API
def request_openmeteo(latitude, longitude):
    openmeteo_params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": ["temperature_2m", "precipitation"],
        "forecast_days": 1
    }

    openmeteo_response = requests.get(URL_OPENMETEO, params=openmeteo_params)

    # check if lack of proper request response is due to 403 or 503 error
    response_errors(openmeteo_response, OPENMETEO_NAME)

    return parse_openmeteo_response(openmeteo_response)


# meteostat.net
def request_meteostat(api_key, latitude, longitude, current_date):
    meteostat_params = {
        "lat": latitude,
        "lon": longitude,
        "start": current_date,  # current day obtained from first api request
        "end": current_date
    }

    meteostat_headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "meteostat.p.rapidapi.com"
    }

    meteostat_response = requests.get(URL_METEOSTAT, headers=meteostat_headers, params=meteostat_params)

    # check if lack of proper request response is due to 403 or 503 error
    response_errors(meteostat_response, METEOSTAT_NAME)

    return parse_meteostat_response(meteostat_response)
