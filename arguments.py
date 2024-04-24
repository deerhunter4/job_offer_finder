import sys
import argparse


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
    parser.add_argument('-fp', metavar='forecast_period', type=str,
                        choices=['24h', '48h', '72h', '7days', '10days', '14days'],
                        help="""Enter the forecast period you are interested
                         in. Valid options are: 24h, 48h, 72h, 7days, 10days,
                         14days (default: 24h).""", default='24h')

    # if no arguments were given, printing the help message (args = "--help")
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    return args
