import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px


class WeatherDashboard:
    def __init__(self, max_temp_date, max_temp, min_temp_date, min_temp, temperature_data, predicted_temp):
        self.max_temp_date = max_temp_date
        self.max_temp = max_temp
        self.min_temp_date = min_temp_date
        self.min_temp = min_temp
        self.temperature_data = temperature_data
        self.predicted_temp = predicted_temp

        # Initialize the Dash app
        self.app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


    def predicted_temp_card(self):
        return dbc.Card(
            [
                dbc.CardHeader("Predicted Temperature"),
                dbc.CardBody(
                    html.H3(f"{self.predicted_temp}°C", className="card-title text-success"),
                ),
            ],
            className="shadow-sm",
        )
    
    def temperature_card(self, title, temperature, date):
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

    def temperature_plot(self):

        return px.line(
            self.temperature_data,
            x="Date",
            y="Value",
            title="Temperature Over Time",
            labels={"Date": "Date", "Value": "Temperature (°C)"},
            template="plotly_white",
        )

    def layout(self):
        fig = self.temperature_plot()

        return dbc.Container(
            [
                # Predicted Temperature
                dbc.Row(
                    [
                        dbc.Col(self.predicted_temp_card(), width=12),
                    ],
                    className="mt-3",
                ),

                # Min and Max Temperature Cards
                dbc.Row(
                    [
                        dbc.Col(self.temperature_card("Min Temperature", self.min_temp, self.min_temp_date), width=4),
                        dbc.Col(self.temperature_card("Max Temperature", self.max_temp, self.max_temp_date), width=4),
                    ],
                    justify="center",
                    className="mt-5",
                ),

                # Line Plot
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(figure=fig), width=10),
                    ],
                    justify="center",
                    className="mt-4",
                ),
            ],
            fluid=True,
            style={"padding": "20px"},
        )

    def run(self, debug=True):
        self.app.layout = self.layout()
        self.app.run_server(debug=debug)
