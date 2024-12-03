import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


def create_dashboard(max_temp_date, max_temp, min_temp_date, min_temp, temperature_data):
    # Initialize the Dash app
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

    # Create the line plot using Plotly
    fig = px.line(
        temperature_data,
        x="Date",
        y="Avg_temperature",
        title="Temperature Over Time",
        labels={"Date": "Date", "Temperature": "Temperature (°C)"},
        template="plotly_white",
    )

    # Define the layout
    app.layout = dbc.Container(
        [
            dbc.Row(
                [
                    # Card for Max Temperature
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardHeader("Max Temperature"),
                                dbc.CardBody(
                                    [
                                        html.H3(f"{max_temp}°C", className="card-title text-primary"),
                                        html.P(f"Date: {max_temp_date}", className="card-text"),
                                    ]
                                ),
                            ],
                            className="shadow-sm",
                        ),
                        width=4,
                    ),
                    # Card for Min Temperature
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardHeader("Min Temperature"),
                                dbc.CardBody(
                                    [
                                        html.H3(f"{min_temp}°C", className="card-title text-primary"),
                                        html.P(f"Date: {min_temp_date}", className="card-text"),
                                    ]
                                ),
                            ],
                            className="shadow-sm",
                        ),
                        width=4,
                    ),
                ],
                justify="center",
                className="mt-5",
            ),
            dbc.Row(
                [
                    # Line Plot
                    dbc.Col(
                        dcc.Graph(figure=fig),
                        width=12,
                    ),
                ],
                className="mt-4",
            ),
        ],
        fluid=True,
    )

    return app
