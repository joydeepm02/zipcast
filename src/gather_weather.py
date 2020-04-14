import os
import json
import urllib.request
from .util import *

def get_weather(zipcode=27513):
	key = os.environ['OWM_API_KEY'] 
	url = 'http://api.openweathermap.org/data/2.5/weather?zip=' + str(zipcode) + '&appid=' + key
	src = urllib.request.urlopen(url).read()
	json_data = json.loads(src.decode('utf-8'))

	data = {
		"location_name" : json_data["name"],
		"location_country" : json_data["sys"]["country"],
		"conditions" : json_data["weather"][0]["main"],
		"temp" : kelvin_to_fahrenheit(json_data["main"]["temp"]),
		"min_temp" : kelvin_to_fahrenheit(json_data["main"]["temp_min"]),
		"max_temp" : kelvin_to_fahrenheit(json_data["main"]["temp_max"]),
		"feels_like_temp" : kelvin_to_fahrenheit(json_data["main"]["feels_like"]),
                "icon" : "http://openweathermap.org/img/wn/" + json_data["weather"][0]["icon"] + "@2x.png"
	}

	return data
