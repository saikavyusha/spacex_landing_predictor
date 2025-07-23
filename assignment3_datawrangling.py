import pandas as pd
import numpy as np

# === Load Datasets ===
api_path = "spacex_launch_data.csv"
wiki_path = "wikipedia_spacex_data.csv"

api_df = pd.read_csv(api_path)
wiki_df = pd.read_csv(wiki_path)

# === Clean Wikipedia Dataset ===
wiki_df['PayloadMass'] = (
    wiki_df['PayloadMass']
    .replace('kg', '', regex=True)
    .replace(',', '', regex=True)
    .replace('—', np.nan)
    .replace('', np.nan)
    .astype(str)
    .str.extract('(\d+\.?\d*)')[0]
    .astype(float)
)

wiki_df_cleaned = wiki_df.dropna(subset=['PayloadMass', 'Orbit', 'LandingOutcome'])
wiki_encoded = pd.get_dummies(wiki_df_cleaned, columns=['Orbit', 'LaunchSite', 'Booster'])
wiki_encoded['LandingOutcome'] = wiki_df_cleaned['LandingOutcome'].str.lower().str.contains("success").astype(int)

# === Clean API Dataset ===
api_df_cleaned = api_df.dropna(subset=['PayloadMass', 'Orbit', 'LandingOutcome'])
api_df_cleaned = api_df_cleaned.rename(columns={'BoosterVersion': 'Booster'})
api_encoded = pd.get_dummies(api_df_cleaned, columns=['Orbit', 'LaunchSite', 'Booster'])
api_encoded['LandingOutcome'] = api_df_cleaned['LandingOutcome'].astype(int)

# === Save Cleaned Outputs ===
wiki_encoded.to_csv("cleaned_wikipedia_dataset.csv", index=False)
api_encoded.to_csv("cleaned_api_dataset.csv", index=False)

print("Assignment 3 complete. Cleaned datasets saved:")
print("→ cleaned_wikipedia_dataset.csv")
print("→ cleaned_api_dataset.csv")
