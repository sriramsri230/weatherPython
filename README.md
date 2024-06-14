# Weather API Flask Application

This is a simple Flask web application that allows users to get current weather information for a specified city using the WeatherAPI.com service.

## Description

The Weather API Flask application allows users to enter a city name and retrieve the current weather conditions for that city. The application fetches weather data from WeatherAPI.com and displays it in a user-friendly format.

## Features

- User-friendly interface to input city names
- Fetches and displays current weather data including temperature, condition, and location
- Simple and clean HTML templates for displaying weather data

## Requirements

- Python 3.x
- Flask
- Requests

## Installation

1. Clone the repository:

    git clone https://github.com/yourusername/weather-api-flask.git
    cd weather-api-flask
  

2. Set up a virtual environment:

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:

    pip install Flask requests

4. Set up your WeatherAPI.com API key:

    Open `app.py` and replace `YOUR_API_KEY` with your actual WeatherAPI.com API key:

    ```python
    API_KEY = "YOUR_API_KEY"
    ```

## Usage

1. Run the Flask application:

    python app.py

2. Open your web browser and navigate to `http://localhost:5000`.

3. Enter a city name in the input field and click "Submit" to view the current weather data for that city.


Used ChatGpt ...
