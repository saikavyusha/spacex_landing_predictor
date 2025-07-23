import pandas as pd
import duckdb

# Load cleaned API dataset
df = pd.read_csv("cleaned_api_dataset.csv")

# Create SQL connection using DuckDB
con = duckdb.connect()

# Register the DataFrame as a SQL table
con.register("spacex", df)

# Query 1: Number of launches per orbit
query1 = "SELECT Orbit_GTO, COUNT(*) AS count FROM spacex GROUP BY Orbit_GTO"
print("\n Launches into GTO Orbit:")
print(con.execute(query1).fetchdf())

# Query 2: Average Payload per Launch Site
query2 = """
SELECT 
    "LaunchSite_CCSFS SLC 40",
    "LaunchSite_KSC LC 39A",
    "LaunchSite_VAFB SLC 4E",
    AVG(PayloadMass) as avg_payload
FROM spacex
GROUP BY 1, 2, 3
"""
print("\n Average Payload Mass per Launch Site:")
print(con.execute(query2).fetchdf())

# Query 3: Landing success rate by Booster type
query3 = """
SELECT 
    "Booster_Falcon 9",
    "Booster_Falcon Heavy",
    AVG(LandingOutcome) as success_rate
FROM spacex
GROUP BY 1, 2
"""
print("\n Landing Success Rate by Booster:")
print(con.execute(query3).fetchdf())

# Optional: Print column names for reference
print("\n Column names:")
print(df.columns.tolist())
