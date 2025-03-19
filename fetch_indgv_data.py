import requests
import pandas as pd
import json

url = "https://webservices.ingv.it/fdsnws/event/1/query"

# Define query parameters (Modify as needed)
params = {
    "starttime": "2025-02-10T00:00:00",
    "endtime": "2025-03-17T23:59:59",
    "minmag": 2,
    "maxmag": 10,
    "mindepth": -10,
    "maxdepth": 1000,
    "minlat": -90,
    "maxlat": 90,
    "minlon": -180,
    "maxlon": 180,
    "format": "geojson",
    "limit": 10000
}

# Fetch data 
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    
    # Extract earthquake events
    features = data.get("features", [])
    
    # Create a DataFrame
    earthquake_data = []
    for event in features:
        props = event.get("properties", {})
        geometry = event.get("geometry", {}).get("coordinates", [None, None, None])
        
        earthquake_data.append({
            "Time": props.get("time"),
            "Latitude": geometry[1],
            "Longitude": geometry[0],
            "Depth_km": geometry[2],
            "Magnitude": props.get("mag"),
            "Region": props.get("place")   
        })
    
    df = pd.DataFrame(earthquake_data)

    # Save data to CSV
    df.to_csv("earthquake_data.csv", index=False)
    

    print("✅ Earthquake data saved as 'earthquake_data.csv'")
else:
    print("❌ Failed to fetch data:", response.status_code, response.text)
