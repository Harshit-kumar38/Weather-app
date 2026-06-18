import requests
from config import API_KEY
from weather_utils import weather_report


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()



city = input('Enter the city: ')
data = get_weather(city)

if data['cod'] == 200:
    weather_report(data)
else:
    print('City not found!')
