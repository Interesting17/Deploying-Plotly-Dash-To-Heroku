import pandas as pd
import dash
import statistics as stc
import datetime as dt 
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from plotly import graph_objects as go
from Traffic_View_Class import Traffic_View as TV

data = pd.read_excel('FootTrafficUpdate.xlsx')
data = data.drop(columns = 'Unnamed: 0')
print(data.columns)


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
server = app.server

app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([
       
    dbc.Row([html.Br(), html.Br(),
             dbc.Col(lg=1),
             #dbc.Col([html.Img(src=app.get_asset_url('saco_logo.png'))], lg= 1),
             dbc.Col([html.Br(), html.Br(), html.Div([html.P("SACO Foot Traffic Dashboard")], style={'textAlign': "center", 'font-size':'300%', 'font-family':'Roboto Condensed', 'font-weight': 'bold'})]),  
             #dbc.Col([html.Img(src=app.get_asset_url('17.png'))], lg= 1),
             dbc.Col(lg=1)
              ])
], style={'backgroundColor': '#eeeee'}) 


    
    if __name__ == '__main__':
    app.run_server()

   
