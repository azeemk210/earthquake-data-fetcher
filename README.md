# Earthquake Data Fetcher

## Overview
This repository contains Python scripts to fetch earthquake data from two different sources:

1. **EMSC (European-Mediterranean Seismological Centre)** - Retrieves earthquake data in CSV format.
2. **INGV (Istituto Nazionale di Geofisica e Vulcanologia, Italy)** - Retrieves earthquake data in GeoJSON format.

## Files
- `fetch_emsc_data.py` - Fetches earthquake data from EMSC API and saves it as a CSV file.
- `fetch_indgv_data.py` - Fetches earthquake data from INGV API and saves it as a CSV file.

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required Python libraries:
  ```sh
  pip install requests pandas
  ```

### Clone the Repository
```sh
git clone https://github.com/your-username/earthquake-data-fetcher.git
cd earthquake-data-fetcher
```

## Usage
### Fetching Earthquake Data
Run the scripts to download and save earthquake data:
```sh
python fetch_emsc_data.py
python fetch_indgv_data.py
```

After execution, earthquake data will be saved as CSV files.

## Contributing
Feel free to submit pull requests with improvements or bug fixes.

## License
This project is open-source and available under the MIT License.
