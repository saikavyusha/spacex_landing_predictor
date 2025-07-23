import requests
import pandas as pd

# Base URLs
launches_url = "https://api.spacexdata.com/v4/launches"
rockets_url = "https://api.spacexdata.com/v4/rockets/"
launchpads_url = "https://api.spacexdata.com/v4/launchpads/"
payloads_url = "https://api.spacexdata.com/v4/payloads/"

# Step 1: Get all launches
launches = requests.get(launches_url).json()

data = []

for launch in launches:
    if not launch['upcoming'] and launch['cores'][0]['landing_success'] is not None:
        rocket_id = launch['rocket']
        launchpad_id = launch['launchpad']
        payload_id = launch['payloads'][0] if launch['payloads'] else None

        # Get rocket name
        rocket = requests.get(rockets_url + rocket_id).json()
        booster = rocket['name']

        # Get launchpad info
        launchpad = requests.get(launchpads_url + launchpad_id).json()
        site = launchpad['name']
        latitude = launchpad['latitude']
        longitude = launchpad['longitude']

        # Get payload info
        payload = requests.get(payloads_url + payload_id).json() if payload_id else {}
        mass_kg = payload.get('mass_kg', None)
        orbit = payload.get('orbit', None)

        # Outcome
        landing_success = launch['cores'][0]['landing_success']

        data.append({
            'BoosterVersion': booster,
            'LaunchSite': site,
            'Latitude': latitude,
            'Longitude': longitude,
            'PayloadMass': mass_kg,
            'Orbit': orbit,
            'LandingOutcome': landing_success
        })

# Convert to DataFrame
df = pd.DataFrame(data)
df.to_csv("spacex_launch_data.csv", index=False)
print("Data saved to spacex_launch_data.csv")
