import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all launch tables
tables = soup.find_all('table', {'class': 'wikitable'})

launch_data = []

for table in tables:
    rows = table.find_all('tr')[1:]  # Skip header
    for row in rows:
        cols = row.find_all(['td', 'th'])
        cols = [ele.text.strip() for ele in cols]

        # Example structure; update once you see real column patterns
        if len(cols) > 5:
            launch_data.append({
                'Date': cols[0],
                'Booster': cols[1],
                'LaunchSite': cols[2],
                'PayloadMass': cols[3],  # Clean/convert if needed
                'Orbit': cols[4],
                'LandingOutcome': cols[5]
            })

# Convert to DataFrame and save
df_wiki = pd.DataFrame(launch_data)
df_wiki.to_csv("wikipedia_spacex_data.csv", index=False)
print("Wikipedia launch data saved.")
