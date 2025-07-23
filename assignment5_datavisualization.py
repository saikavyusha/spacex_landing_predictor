import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the cleaned API dataset
df = pd.read_csv("cleaned_api_dataset.csv")

# === 1. Bar Plot: Number of Launches by Booster Type ===
booster_counts = df[['Booster_Falcon 9', 'Booster_Falcon Heavy']].sum()
booster_counts.plot(kind='bar', title='🚀 Number of Launches by Booster Type', color=['skyblue', 'orange'])
plt.ylabel('Launch Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# === 2. Pie Chart: Orbit Type Distribution ===
orbit_cols = [col for col in df.columns if col.startswith('Orbit_')]
orbit_counts = df[orbit_cols].sum()
orbit_counts.plot.pie(autopct='%1.1f%%', figsize=(6, 6), title='🛰 Orbit Distribution')
plt.ylabel('')
plt.show()

# === 3. Boxplot: Payload Mass by Launch Site ===
site_cols = [col for col in df.columns if col.startswith('LaunchSite_')]
melted = pd.melt(df, id_vars='PayloadMass', value_vars=site_cols, var_name='LaunchSite', value_name='Launched')
melted = melted[melted['Launched'] == 1]
sns.boxplot(data=melted, x='LaunchSite', y='PayloadMass')
plt.title(" Payload Mass Distribution by Launch Site")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# === 4. Histogram: Payload Mass Distribution ===
plt.hist(df['PayloadMass'], bins=20, color='purple', edgecolor='black')
plt.title('Payload Mass Distribution')
plt.xlabel('Payload (kg)')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()
