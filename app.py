from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv('WEATHER_API_KEY', '9ce096df439c47308ad65258242303')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'city': data['location']['name'],
            'country': data['location']['country'],
            'temperature': data['current']['temp_c'],
            'condition': data['current']['condition']['text'],
            'icon': data['current']['condition']['icon'].replace('//cdn.weatherapi.com/', 'https://cdn.weatherapi.com/'),  # Replace with direct color icon URL if available
            'humidity': data['current']['humidity'],
            'wind_speed': data['current']['wind_kph'],
            'wind_dir': data['current']['wind_dir'],
            'feels_like': data['current']['feelslike_c'],
            'visibility': data['current']['vis_km']
        }

        return render_template('weather.html', weather=weather_data)
    else:
        return f"Error fetching data: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
