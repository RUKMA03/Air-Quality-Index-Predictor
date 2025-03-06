import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import dotenv

# Load environment variables
dotenv.load_dotenv()

app = Flask(__name__)
CORS(app)

# Get token from .env file
token = os.getenv("WAQI_TOKEN")

@app.route('/api/api_req', methods=['GET'])
def get_air_quality():
    city = request.args.get('city')
    url = f"https://api.waqi.info/feed/{city}/?token={token}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'ok':
            return jsonify(data['data'])
        else:
            return jsonify({'error': data['data']}), 400
    else:
        return jsonify({'error': 'Failed to fetch data from WAQI API'}), response.status_code

if __name__ == '__main__':
    # Running the app on port 8000
    app.run(debug=True, port=8000)
