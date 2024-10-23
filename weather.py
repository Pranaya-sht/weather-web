import requests
from dotenv import load_dotenv
import os 
from pprint import pprint

load_dotenv()

def get_current_weather(city="kathmandu"):
    api_key=os.getenv("API_KEY")
    request_url=f'https://api.openweathermap.org/data/2.5/weather?&appid={api_key}&q={city}&units=metric'
    weather_data =requests.get(request_url).json()
    return weather_data
    
    


    
   
   
    
   
    
    # print(f'\ncurrent weather for {weather_data["name"]}')
    # print(f'\nthe temp is  {weather_data["main"]["temp"] }°C')
    # print(f'\nFeels like {weather_data["main"]["feels_like"]}°C and {weather_data["weather"][0]["description"].capitalize()}.')
   
if __name__ == "__main__":
    print('\n****************get weather condition********************\n')
    
    city =input("\n Please enter a city name:\n")
    # chack for empty strings
    if not bool(city.strip()):
        city="Kathmandu"
    weather_data=get_current_weather(city)
    print("\n")
    pprint(weather_data)  