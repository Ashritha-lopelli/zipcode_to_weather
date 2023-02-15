from flask import Flask, jsonify
import requests

app = Flask(__name__)

zip_codes = [
    {
        "weather": "Cloudy",
        "zip_code": "10001"
    },
    {
        "weather": "Sunny",
        "zip_code": "90001"
    },
    {
        "weather": "Snow",
        "zip_code": "60601"
    }
]
@app.route("/weather/<city>")
def get_weather(city):
    zip_code = requests.get(f"http://localhost:5003/zipcodes/{city}/zipcode")
    zip_code_1 = zip_code.text
    for zip_code in zip_codes:
            if zip_code['zip_code'] == zip_code_1:
                return zip_code['weather']
    return "weather not found"
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port =5004)
