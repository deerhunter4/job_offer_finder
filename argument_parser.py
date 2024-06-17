import sys
import argparse
from datetime import date, datetime

LOCATION_ARG = "-location"
PERIOD_ARG = "-fp"
AVALAIBLE_PERIODS = ['24h', '48h', '72h', '7days', '10days', '14days']
DATE_ARG = "-date"
TEMP_ARG = "-temp"
AVALAIBLE_TEMP = ['C', 'F']
WEATHER_ARG = '-weather_components'
ADDITIONAL_WEATHER_PARAM = ['wind', 'pressure', 'both']


def check_args(args):
    args_iterable = iter(args)
    args_dict = dict(zip(args_iterable, args_iterable))

    if LOCATION_ARG not in args_dict:
        raise ValueError("Location argument has not been provided!")

    if PERIOD_ARG in args_dict and args_dict[PERIOD_ARG] not in AVALAIBLE_PERIODS:
        raise ValueError("""Entered forecast_period value is not allowed.
                         Valid options are: 24h, 48h, 72h, 7days, 10days, 14days
                         (default: 24h).""")

    if DATE_ARG in args_dict:
        try:
            datetime.strptime(args_dict[DATE_ARG], '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD.")

    if TEMP_ARG in args_dict and args_dict[TEMP_ARG] not in AVALAIBLE_TEMP:
        raise ValueError("""Select the Celsius [C] or Fahrenheit [F]
                         temperature scale (default: C).""")

    if WEATHER_ARG in args_dict and args_dict[WEATHER_ARG] not in ADDITIONAL_WEATHER_PARAM:
        raise ValueError("""Select additional weather components that you are
                        interested in. Valid options are: wind and pressure.""")


# get parameters that will be used by the requester component
def get_parameters():
    check_args(sys.argv[1:])

    current_date = str(date.today())
    print(current_date)

    parser = argparse.ArgumentParser(
            prog='BetterWeather',
            description="""
            Purpose of the program is to collect weather forecast data
            from a few free weather forecast APIs (e.g. Open-Meteo, WeatherAPI)
            and combine it into one more accurate weather prediction.
            After providing the location eg. "Madrid" you will receive a file
            with weather data and a user-friendly plot.""")

    # positional arguments
    parser.add_argument('-location', metavar='location', type=str,
                        help="""Enter the location for which you want
                         to get the weather forecast e.g. "Cracovia".""")

    # optional arguments
    parser.add_argument('-fp', metavar='forecast_period', type=str,
                        choices=['24h', '48h', '72h', '7days', '10days', '14days'],
                        help="""Enter the forecast period you are interested
                         in. Valid options are: 24h, 48h, 72h, 7days, 10days,
                         14days (default: 24h).""", default='24h')

    parser.add_argument('-date', metavar='date', type=str, help="""Enter
                        date for which the weather forecast will be generated.
                        The correct format should be YYYY-MM-DD""",
                        default=current_date)

    parser.add_argument('-temperature', metavar='temperature', type=str,
                        choices=AVALAIBLE_TEMP, help="""Select the Celsius [C]
                        or Fahrenheit [F] temperature scale (default: C).""",
                        default='C')

    parser.add_argument('-weather_components', metavar='weather_components',
                        type=str, choices=ADDITIONAL_WEATHER_PARAM,
                        help="""Selectadditional weather components that you
                        are interested in. Valid options are: wind,
                        pressure and both.""")

    args = parser.parse_args()
    return [args, current_date]
