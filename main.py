from argument_parser import get_parameters
from key_reader import get_keys
from api_requester import request_weatherapi, request_openmeteo, request_meteostat, WEATHERAPI_NAME, METEOSTAT_NAME
from api_response_parser import get_coordinates, parse_weatherapi_response
from data_transformer import create_dataframe
from file_writer import write_csv
from plot import create_plot

if __name__ == "__main__":

    parameters, current_date = get_parameters()
    print(f"Parameters used for API request are {parameters}")

    # get API keys from the file
    keys = get_keys()
    print(f"The API keys have correct names:\n{list(keys.keys())}")

    # request to wheatherapi; get latitude and longitude of the location
    # weatherapi_forecast, [latitude, longitude] = request_weatherapi(keys[WEATHERAPI_NAME], parameters)
    weatherapi_response = request_weatherapi(keys[WEATHERAPI_NAME], parameters)
    [latitude, longitude] = get_coordinates(weatherapi_response)
    weatherapi_forecast = parse_weatherapi_response(weatherapi_response)
    print("\nweatherapi forecast\n")
    print(weatherapi_forecast)

    # request to wheatherapi
    openmeteo_forecast = request_openmeteo(latitude, longitude)
    print("\nopenmeteo forecast\n")
    print(openmeteo_forecast)

    # request to meteostat
    meteostat_forecast = request_meteostat(keys[METEOSTAT_NAME], latitude, longitude, parameters.date)
    print("\nmeteostat forecast\n")
    print(meteostat_forecast)

    # create dataframe from diccionaries
    dataframe = create_dataframe(weatherapi_forecast, openmeteo_forecast, meteostat_forecast)
    print(dataframe)

    # save dataframe as CSV file
    write_csv(dataframe, parameters)

    # create plot 
    create_plot(dataframe, parameters)
