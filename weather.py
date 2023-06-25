import datetime as dt
import requests
import os

BASE_URL="http://api.openweathermap.org/data/2.5/weather?"

#create a text file having spi key 
#API_KEY=open('api_key.txt','r').read() 

#setup of environment variables for apikey
user_api = os.environ['current_weather_data']
location = input("Enter the city name: ")

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius=kelvin-273.15
    fahrenheit=celsius*(9/5)+32
    return celsius,fahrenheit

url=BASE_URL+ "appid="+ user_api+ "&q="+ location
response=requests.get(url).json()
print(response)

temp_kelvin=response['main']['temp']
temp_celsius,temp_fahrenheit=kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin=response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit=kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed=response['wind']['speed']
humidity=response['main']['humidity']
description=response['weather'][0]['description']
sunrise_time=dt.datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone'])
sunset_time=dt.datetime.utcfromtimestamp(response['sys']['sunset']+response['timezone'])
print(f"Temperature in {location}: {temp_celsius:.2f}°C or {temp_fahrenheit}°F")
print(f"Temperature in {location} feels like : {feels_like_celsius:.2f}°C or {feels_like_fahrenheit}°F")
print(f"Humidity in {location}: {humidity}%")
print(f"Wind speed in {location}: {wind_speed}m/s")
print(f"Sunrises in in {location} at {sunrise_time} local time.")
print(f"Sunsets in in {location} at {sunset_time} local time.")
print(f"General weather in {location}: {description}")

