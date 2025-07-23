import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("cleaned_api_dataset.csv")

# Create a new column to map actual site name for easier filtering
df['LaunchSite'] = df.apply(
    lambda row: 'CCSFS SLC 40' if row['LaunchSite_CCSFS SLC 40'] == 1 else (
                'KSC LC 39A' if row['LaunchSite_KSC LC 39A'] == 1 else (
                'VAFB SLC 4E' if row['LaunchSite_VAFB SLC 4E'] == 1 else 'Unknown')),
    axis=1
)

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "SpaceX Launch Dashboard"

# App layout
app.layout = html.Div([
    html.H1("SpaceX Launch Dashboard", style={'textAlign': 'center'}),

    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'},
            {'label': 'CCSFS SLC 40', 'value': 'CCSFS SLC 40'},
            {'label': 'KSC LC 39A', 'value': 'KSC LC 39A'},
            {'label': 'VAFB SLC 4E', 'value': 'VAFB SLC 4E'}
        ],
        value='ALL',
        placeholder="Select a Launch Site",
        searchable=True,
        style={'width': '50%', 'margin': '0 auto'}
    ),

    html.Br(),

    dcc.Graph(id='success-pie-chart'),

    html.Br(),

    dcc.Graph(id='payload-scatter-chart')
])

# Callback for pie chart
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_pie(selected_site):
    if selected_site == 'ALL':
        fig = px.pie(
            df,
            names='LandingOutcome',
            title='Overall Landing Success Rate'
        )
    else:
        filtered_df = df[df['LaunchSite'] == selected_site]
        fig = px.pie(
            filtered_df,
            names='LandingOutcome',
            title=f"Landing Success Rate for {selected_site}"
        )
    return fig

# Callback for scatter plot
@app.callback(
    Output('payload-scatter-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_scatter(selected_site):
    if selected_site == 'ALL':
        filtered_df = df
        title = "Payload Mass vs. Outcome (All Sites)"
    else:
        filtered_df = df[df['LaunchSite'] == selected_site]
        title = f"Payload Mass vs. Outcome at {selected_site}"

    fig = px.scatter(
        filtered_df,
        x='PayloadMass',
        y='LandingOutcome',
        color='LandingOutcome',
        hover_data=['Booster_Falcon 9', 'Booster_Falcon Heavy'],
        title=title
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
