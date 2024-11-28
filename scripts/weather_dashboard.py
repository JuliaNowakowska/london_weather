import dash
from dash import dcc, html
import dash_bootstrap_components as dbc


def create_dashboard(max_temp_date, max_temp, min_temp_date, min_temp):
    # Initialize the Dash app
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

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
        ],
        fluid=True,
    )

    return app


