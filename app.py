from flask import Flask, jsonify
import requests

app = Flask(__name__)
api_key = "e18ee1b6e5331e253852aa61412d618e"  # Replace with your OpenWeatherMap API key
@app.route("/weather/<city>")
def get_weather(city):
    # Make a request to the OpenWeatherMap API
    zip_code = f"http://localhost:5003/zipcodes/{city}/zipcode"
    url = f"http://api.openweathermap.org/data/2.5/forecast?zip={zip_code},us&appid={api_key}"
    response = requests.get(url)

    # Check the response status code
    if response.status_code == 200:
        weather_data = response.json()
        return jsonify(weather_data)
    else:
        return "Error retrieving weather data", response.status_code

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port =5004)
