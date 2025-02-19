import os
from datetime import datetime
from flask import Blueprint, render_template, request
import requests

# Create a blueprint
main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    forecast_data = None
    error_message = None

    if request.method == 'POST':
        city = request.form.get('city')
        state = request.form.get('state')
        country = request.form.get('country')

        if city and country:
            api_key = os.getenv('WEATHER_KEY')  # I saved my key in .env file
            print(api_key)  # This will print the key in the console or None

            # Current weather API call
            url = (f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},"
                   f"{country}&appid={api_key}&units=metric")
            response = requests.get(url)
            print(response.text)
            if response.status_code == 200:
                weather_data = response.json()
                # Convert the Unix timestamp to the desired format
                weather_data['formatted_time'] = datetime.utcfromtimestamp(weather_data['dt']).strftime(
                    '%-I:%M %p').lower()
            else:
                error_message = "Unable to fetch weather data. Please check your inputs."

            # Forecast API call
            forecast_url = (f"https://api.openweathermap.org/data/2.5/forecast?q={city},{state},"
                            f"{country}&appid={api_key}&units=metric")
            forecast_response = requests.get(forecast_url)
            print(forecast_response.text)
            if forecast_response.status_code == 200:
                forecast_data = forecast_response.json()
            else:
                error_message = "No forecast found."
        else:
            error_message = "City and Country are required."

    return render_template('dashboard.html', weather_data=weather_data, forecast_data=forecast_data,
                           error_message=error_message)
