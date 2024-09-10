from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Function to get weather data
def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    
    # Check if the response was successful
    if response.status_code == 200:
        return response.json()
    else:
        return None

# API Key (Replace with your actual API key)
api_key = "97c00a28dcf736a0ff231206d5ca3684"

# Home route
@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    if request.method == 'POST':
        location = request.form.get('location')
        if location:
            weather_data = get_weather(api_key, location)
            if not weather_data:
                weather_data = {'error': 'Unable to fetch weather data. Please try again.'}
    
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
