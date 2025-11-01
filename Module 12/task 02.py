import json
import requests

city = input("Enter City: ")

api_key = input("Enter API Key:")

#API KEY: 04a09b4e9dcef12be387506d643f6e9d or try
# 2nd API KEY: 1ed4d804f517492ac30010c67b041bf1

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    weather = data["weather"][0]["description"]
    temperature_kelvin = data["main"]["temp"]
    temperature_celsius = temperature_kelvin - 273.15

    print(f'\nWeather in {city}: {weather}')
    print(f'Temperature in Celsius: {temperature_celsius:.1f}')

else:
    print('Error:', data.get('message', 'Unable to fetch data'))
