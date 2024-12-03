import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px


def create_temperature_card(title, temperature, date):
    return dbc.Card(
        [
            dbc.CardHeader(title),
            dbc.CardBody(
                [
                    html.H3(f"{temperature}°C", className="card-title text-primary"),
                    html.P(f"Date: {date}", className="card-text"),
                ]
            ),
        ],
        className="shadow-sm",
    )

def create_temperature_plot(data):
    return px.line(
        data,
        x="Date",
        y="Value",
        title="Temperature Over Time",
        labels={"Date": "Date", "Value": "Temperature (°C)"},
        template="plotly_white",
    )

def create_dashboard_layout(max_temp_date, max_temp, min_temp_date, min_temp, temperature_data):
    # Generating the figure with temp plot
    fig = create_temperature_plot(temperature_data)

    # Defining the layout
    layout = dbc.Container(
        [
            dbc.Row(
                [
                    # Min Temperature Card
                    dbc.Col(create_temperature_card("Min Temperature", min_temp, min_temp_date), width=4),
                    # Max Temperature Card
                    dbc.Col(create_temperature_card("Max Temperature", max_temp, max_temp_date), width=4),
                ],
                justify="center",
                className="mt-5",
            ),
            dbc.Row(
                [
                    # Line Plot with monthly average temperature
                    dbc.Col(dcc.Graph(figure=fig), width=12),
                ],
                className="mt-4",
            ),
        ],
        fluid=True,
    )
    return layout

# Main function
def create_dashboard(max_temp_date, max_temp, min_temp_date, min_temp, temperature_data):
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = create_dashboard_layout(max_temp_date, max_temp, min_temp_date, min_temp, temperature_data)
    return app
