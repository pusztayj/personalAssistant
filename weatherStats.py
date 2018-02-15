"""
Authors: Justin Pusztay and Trevor Stalnaker
File: weatherStats.py
Version 1
"""

import datetime
import json
import urllib.request

def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time

#Here is where I add the different types of URLs ie zipcode, gps coordinates
def url_builder(city_id):
    user_api = 'f122fc304e6dc9181e7ea944c715c8a2'  
    unit = 'metric'  #Fahrenheit-imperial, Celsius-metric, Kelvin-default
    city = city_id
    api = 'http://api.openweathermap.org/data/2.5/weather?q='     
    full_api_url = api + city + '&mode=json&units=' + unit + '&APPID=' + user_api
    return full_api_url

def data_fetch(full_api_url):
    url = urllib.request.urlopen(full_api_url)
    output = url.read().decode('utf-8')
    raw_api_dict = json.loads(output)
    url.close()
    print(output)
    return raw_api_dict

def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        humidity=raw_api_dict.get('main').get('humidity'),
        pressure=raw_api_dict.get('main').get('pressure'),
        sky=raw_api_dict['weather'][0]['main'],
        sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
        sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
        wind=raw_api_dict.get('wind').get('speed'),
        wind_deg=raw_api_dict.get('deg'),
        dt=time_converter(raw_api_dict.get('dt')),
        cloudiness=raw_api_dict.get('clouds').get('all')
    )
    return data


"""
A class the acts as a container for weather data.
Accepts a location as an argument and supplies weather data.
"""
class WeatherStats():

    """Creates a WeatherStats Object"""
    def __init__(self, city_id):
        self._data = data_organizer(data_fetch(url_builder(city_id)))

    """
    Returns a specific attribute from a WeatherStats object.

    Available Attribues: city, country, temp, sky, temp_max, temp_min, wind, wind_deg,
                         humidity, cloudiness, pressure, sunrise, sunset, dt
    """
    def getAttribute(self, attribute):
        return str(self._data[attribute])

    """Returns a string representation of a WeatherStats object"""
    def __str__(self):
        m_symbol = '\xb0' + 'C'
        tempStr = '---------------------------------------\n'
        tempStr += str('Current weather in: {}, {}:'.format(self._data['city'], self._data['country']) + "\n")
        tempStr += str(self._data['temp']) + m_symbol + " " + str(self._data['sky']) + "\n"
        tempStr += str('Max: {}, Min: {}'.format(self._data['temp_max'], self._data['temp_min']) + "\n")
        tempStr += '\n'
        tempStr += str('Wind Speed: {}, Degree: {}'.format(self._data['wind'], self._data['wind_deg']) + "\n")
        tempStr += str('Humidity: {}'.format(self._data['humidity']) + "\n")
        tempStr += str('Cloud: {}'.format(self._data['cloudiness']) + "\n")
        tempStr += str('Pressure: {}'.format(self._data['pressure']) + "\n")
        tempStr += str('Sunrise at: {}'.format(self._data['sunrise']) + "\n")
        tempStr += str('Sunset at: {}'.format(self._data['sunset']) + "\n")
        tempStr += '\n'
        tempStr += str('Last update from the server: {}'.format(self._data['dt']) + "\n")
        tempStr += '---------------------------------------'
        return tempStr

    
    
