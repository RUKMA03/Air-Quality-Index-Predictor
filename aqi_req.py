import requests
import pandas as pd

# Function to fetch air quality data from the WAQI API
def fetch_air_quality_data(city, token):
    url = f"https://api.waqi.info/feed/{city}/?token={token}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'ok':
            return data['data']
        else:
            print("Error fetching data:", data['data'])
    else:
        print("Failed to fetch data. Status code:", response.status_code)
    return None

# Function to clean and format the data
def clean_air_quality_data(data):
    # Extract relevant information
    aqi = data.get('aqi', 'N/A')
    city_name = data['city']['name']
    pollutants = data.get('iaqi', {})
    
    # Create a DataFrame for cleaner display
    cleaned_data = {
        'City': city_name,
        'AQI': aqi,
    }
    
    # Add pollutant data
    for pollutant, value in pollutants.items():
        cleaned_data[pollutant.upper()] = value.get('v', 'N/A')

    df = pd.DataFrame([cleaned_data])
    return df

# Main function to run the program
def main():
    while True:
        city = input("Enter the city name or coordinates (geo:lat;lon): ")

        if (city == "end"):
            break

        token = "ecb06e434ead402651a2901d6bdd3d5032a4cd8e"

        # Fetch and clean data
        air_quality_data = fetch_air_quality_data(city, token)
        if air_quality_data:
            cleaned_df = clean_air_quality_data(air_quality_data)
            print("\nAir Quality Data:")
            print(cleaned_df)
            print("-"*100)

if __name__ == "__main__":
    main()