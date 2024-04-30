import sys
import argparse

# Error printed if entered forecast_period value was not allowed


def forecast_period(name):
    if name in ['24h', '48h', '72h', '7days', '10days', '14days']:
        return name
    else:
        print("""ArgumentError: Entered forecast_period value is not allowed.
              Valid options are: 24h, 48h, 72h, 7days, 10days, 14days
              (default: 24h).""")
        exit()

# get parameters that will be used by the requester component


def parameters():
    parser = argparse.ArgumentParser(
            prog='BetterWeather',
            description="""
            Purpose of the program is to collect weather forecast data
            from a few free weather forecast APIs (e.g. Open-Meteo, WeatherAPI)
            and combine it into one more accurate weather prediction.
            After providing the location eg. "Madrid" you will receive a file
            with weather data and a user-friendly plot.""")

    # positional arguments
    parser.add_argument('location', metavar='location', type=str,
                        help="""Enter the location for which you want
                         to get the weather forecast e.g. "Cracovia".""")

    # optional arguments
    parser.add_argument('-fp', metavar='forecast_period', type=forecast_period,
                        choices=['24h', '48h', '72h', '7days', '10days', '14days'],
                        help="""Enter the forecast period you are interested
                         in. Valid options are: 24h, 48h, 72h, 7days, 10days,
                         14days (default: 24h).""", default='24h')

    # if no arguments were given, the error message is printed
    if not sys.argv[1:]:
        print("""ArgumentError: Location argument has not been provided.""")
        exit()
    args = parser.parse_args()
    return args
