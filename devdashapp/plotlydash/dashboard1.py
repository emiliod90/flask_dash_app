import dash
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import csv
import requests


ticker_url = 'https://storage.googleapis.com/emilio-public-bucket/etf_data/uk/eqqq.csv'


def parse_etf_data(ticker_url):
    # First section of code specific for demo
    with requests.Session() as s:
        download = s.get(ticker_url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        data = list(cr)
        timestamp = []
        o = []
        h = []
        l = []
        ac = []
        vol = []
        for row in data:
            timestamp.append(row[0])
            o.append(row[1])
            h.append(row[2])
            l.append(row[3])
            ac.append(row[5])
            vol.append(row[6])

        return timestamp[1:], o[1:], h[1:], l[1:], ac[1:], vol[1:]


t, o, h, l, c, v = parse_etf_data(ticker_url)


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
                id='candlestick',
                figure={
                    'data': [
                        {'x': t, 'open': o, 'high': h, 'low': l, 'close': c, 'type': 'candlestick'},

                    ],
                    'layout': {
                        'title': '100 Day Candlestick'
                    }
                }
            ),
        ],
        id='dash-container')

    return dash_app.server
