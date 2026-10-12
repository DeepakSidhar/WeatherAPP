

# Import Flask and jsonify
from flask import Flask, jsonify

# Create Flask app
app = Flask(__name__)


# Sample weather data dictionary
# Structure: {'cityname': {'city': 'City Name', 'temperature': 72, ...}}

Cities_dic = {
    "london" : {"city": "London",
        "condition": "Cloudy",
        "temperature": 16,
        "unit": "celsius"},

               }

# Home endpoint - shows API info
@app.route('/')
def home():
    return jsonify({
        "message": "weather APP!",
        "endpoints": [
            "/london",
            "/new york",
            "/tokyo",
            "/paris",
            "/sydney",
            "/weather/all"
        ]

    })

# Return JSON with API information


# Weather endpoint for specific city
@app.route("/weather/<city_name>")
def  get_weather(city_name):

    # Convert city to lowercase
    request_city = city_name.lower()
    print(request_city)
    # Check if city exists in data
    for i in Cities_dic.values():
        if i["city"].lower() == request_city:
            return jsonify(i)
    # If not found, return error (404)
    return jsonify({ "error": "City not found"}), 404



# Endpoint to get all cities' weather
@app.route('/weather/all')
def get_cities():
    # Return JSON with all cities
    return jsonify(list(Cities_dic))





# Run the Flask app

# Print startup information
print("Starting the Application!!!!! ")

# Start server on port 5000

if __name__ == '__main__':
    app.run(debug=True)

