import pandas as pd
import folium

# Load cleaned API dataset
df = pd.read_csv("cleaned_api_dataset.csv")

# Create base map centered on USA
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
spacex_map = folium.Map(location=map_center, zoom_start=4)

# Add circle markers for each launch
for _, row in df.iterrows():
    location = [row['Latitude'], row['Longitude']]
    
    # Color based on success (green = success, red = failure)
    color = 'green' if row['LandingOutcome'] == 1 else 'red'

    folium.CircleMarker(
        location=location,
        radius=6,
        color=color,
        fill=True,
        fill_opacity=0.7,
        popup=f"Payload: {row['PayloadMass']} kg"
    ).add_to(spacex_map)

# Save to HTML
spacex_map.save("spacex_launch_map.html")
print("Map saved: spacex_launch_map.html")
