# Better_Weather

This program is written in Python. Its purpose is to collect weather forecast data from a few websites (e.g. Open-Meteo, WeatherAPI) and combine it into one more accurate weather prediction. After providing the location eg. "Madrid" you will receive a file with weather data and a user-friendly plot. The file will contain raw forecast data acquired from web pages and counted mean values. The plot file will contain hourly temperature and precipitation graph.


**Requirements:**

You need to register yourself on few websites (list below) to receive an API key:
- https://www.weatherapi.com/signup.aspx
- https://rapidapi.com/meteostat/api/meteostat/pricing # choose 'plan basic'

The keys will generated automaticly and will be available after login to your account on sites:
- for weatherapi: https://www.weatherapi.com/docs/#intro-getting-started
- for rapidapi: https://docs.rapidapi.com/docs/keys-and-key-rotation#how-to-find-your-api-key

Create better_weather_keys.txt file that will store your api keys generated in previous steps.
The file should contain the name of the website followed by the appropriate API key separated by a comma, e.g:  
```
weatherapi.com,9b27197b46d...b142443242202  
meteostat.net,5cc4a3480mshd9...p111424jsn9e365e801bf8
```

**Preconditions:**  
Python version: 3.12  
Python packages: argparse, requests, pandas, TBU

**Usage (Linux):**  
Example of basic usage:  
`python3 main.py -location <city>`

Example of optional arguments usage:  
`python3 main.py -location “New York” -forecast_period 72h -date 12-06-2024`

**Usage (Windows)**  
Running a program in Windows powershell with the above code might give an error. In that case check if Python3 is installed, by typing `python --version`. If yes, then run the above code again changing 'python3' to 'python'.

More detailed information can be found in [Better Weather App - feature document](https://docs.google.com/document/d/1BwLEyIXszuNKcbiCdtWt22Z8ZKOX6ePOV2JH_O4gA0I/edit?usp=sharing).

**Note:**  
App is still under development. So far avalaible optional arguments values are: '24h' for forecast_period and current date for date.
