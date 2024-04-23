
# Project Title: Weather App (Command Line Interface)

import requests
import json

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    api_key = "3faa7cb5e309f03ec069068051adb03b"  # Replace "YOUR_API_KEY" with your OpenWeatherMap API key
    city = input("Enter city name: ")
    weather_data = get_weather(api_key, city)
    
    if weather_data["cod"] == 200:
        print(f"Weather in {city}:")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("City not found. Please enter a valid city name.")

if __name__ == "__main__":
    main()


