import requests
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
from pprint import pprint
from waitress import serve

load_dotenv()

def get_current_weather(city="kathmandu"):
    api_key = os.getenv("API_KEY")
    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={api_key}&q={city}&units=metric'
    weather_data = requests.get(request_url).json()
    return weather_data

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():  
    city = request.args.get('city')
    
    # chack for empty strings
    if not bool(city.strip()):
        city="Kathmandu"
        
    weather_data = get_current_weather(city)
    
    #City is not found by API
    if not  weather_data['cod']==200:
        return render_template('city-not-found.html')
    
    return render_template(
       "weather.html",
       title=weather_data["name"],
       status=weather_data["weather"][0]["description"].capitalize(),
       temp=f"{weather_data['main']['temp']:.1f}",
       feels_like=f"{weather_data['main']['feels_like']:.2f}"
    )

if __name__ == "__main__":
    # For local development
    app.run(host="0.0.0.0", port=8000)
    # For production with waitress
    # serve(app, host="0.0.0.0", port=8000)
