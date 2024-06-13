from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "9ce096df439c47308ad65258242303"

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
        location = data['location']['name']
        country = data['location']['country']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        weather_data = {
            'city': location,
            'country': country,
            'temperature': temp_c,
            'condition': condition
        }

        return render_template('weather.html', weather=weather_data)
    else:
        return f"Error fetching data: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True,port=5001)
