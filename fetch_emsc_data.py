import requests
import pandas as pd
import csv
from io import StringIO

# Define the base URL and parameters for the request
url = "http://www.seismicportal.eu/fdsnws/event/1/query"
params = {
    "start": "2017-09-01",
    "end": "2017-11-01",
    "minmag": 6.5,
    "format": "text"
}

# Function to fetch data from the URL
def get_data(url, params):
    response = requests.get(url, params=params, timeout=15)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None


# Function to parse the CSV-formatted response
def parse_csv(data):
    parsed_data = []
    if data:
        csv_reader = csv.reader(StringIO(data), delimiter='|')
        header = next(csv_reader)  # Extract the header row
        
        # Extract required columns
        for row in csv_reader:
            parsed_data.append([
                row[1],  # Time
                float(row[2]),  # Latitude
                float(row[3]),  # Longitude
                float(row[4]),  # Depth (km)
                float(row[10]),  # Magnitude
                row[12]  # Region
            ])
    return parsed_data

# Fetch data
raw_data = get_data(url, params)

# Parse the data
earthquake_data = parse_csv(raw_data)

# Convert to DataFrame
df = pd.DataFrame(earthquake_data, columns=["Time", "Latitude", "Longitude", "Depth_km", "Magnitude", "Region"])

# Save to CSV
csv_filename = "earthquake_data.csv"
df.to_csv(csv_filename, index=False)

print(f"✅ Earthquake data saved as '{csv_filename}'")
