import dash
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import csv


ticker_url = './data/etf/uk/agbp.csv'


def parse_etf_data(ticker_url):
    # Normally this will point to an API endpoint
    # Instead it points to a Local csv file

    # First section of code specific for demo
    with open(ticker_url, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = list(csv_reader)
        timestamp = []
        ac = []
        vol = []
        for row in data:
            timestamp.append(row[0])
            ac.append(row[5])
            vol.append(row[6])

        return timestamp, ac, vol


t, c, v = parse_etf_data(ticker_url)


def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        # external_stylesheets=[
        #     '/static/dist/css/styles.css',
        # ]
    )

    # Create Dash Layout
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                id='volume-bar',
                figure={
                    'data': [
                        {'x': t, 'y': v, 'type': 'bar'},

                    ],
                    'layout': {
                        'title': '100 Day Volume'
                    }
                }
            ),
            dcc.Graph(
                id='close-line',
                figure={
                    'data': [
                        {'x': t, 'y': c, 'type': 'line'},

                    ],
                    'layout': {
                        'title': '100 Day Close'
                    }
                }
            ),
            dcc.Graph(
                id='close-line',
                figure={
                    'data': [
                        {'x': t, 'y': c, 'type': 'line'},

                    ],
                    'layout': {
                        'title': '100 Day Close'
                    }
                }
            ),
            ],
        id='dash-container')

    return dash_app.server
