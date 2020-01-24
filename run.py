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


indexNames = data[ data['Traffic'] == 'Not Working' ].index
data.drop(indexNames , inplace=True)

#image_saco = 'saco_logo.jpg'
#image_17 = '17.png'

for i in range(data.shape[0]):
    if data.iloc[i,5] == 1:
        data.iloc[i,7] = 2020
        
print(data)



date = data['Date']
date = list(dict.fromkeys(date))
#print(date)
dic_date = dict()
for i in date:
    dic_date[i] = 0
    
list_dates = list(dic_date.keys())
#print(list_dates)

data_Central = data[data['Region'] == 'Central']
data_Western = data[data['Region'] == 'Western']
data_Eastern = data[data['Region'] == 'Eastern']


List_Traffic_Central = []
for i in date:
    dic_date[i] = 0
for k in dic_date:
     for i in range(data_Central.shape[0]):            
        if str(data_Central.iloc[i,3]) == str(k):            
            dic_date[k] = dic_date[k] + int(data_Central.iloc[i,1])
     List_Traffic_Central.append(dic_date[k])      

Sum_Central = 0    
for i in List_Traffic_Central:
    Sum_Central = Sum_Central + i    
#print(List_Traffic_Central)

List_Traffic_Western = []
for i in date:
    dic_date[i] = 0
for k in dic_date:
     for i in range(data_Western.shape[0]):            
        if str(data_Western.iloc[i,3]) == str(k):            
            dic_date[k] = dic_date[k] + int(data_Western.iloc[i,1])
     List_Traffic_Western.append(dic_date[k])      
    
Sum_Western = 0 
for i in List_Traffic_Western: 
     Sum_Western = Sum_Western + i    
#print(List_Traffic_Western)


List_Traffic_Eastern = []
for i in date:
    dic_date[i] = 0
for k in dic_date:
     for i in range(data_Eastern.shape[0]):            
        if str(data_Eastern.iloc[i,3]) == str(k):            
            dic_date[k] = dic_date[k] + int(data_Eastern.iloc[i,1])
     List_Traffic_Eastern.append(dic_date[k])      
    
Sum_Eastern = 0
for i in List_Traffic_Eastern:
     Sum_Eastern = Sum_Eastern + i     
#print(List_Traffic_Eastern)

List_Traffic_All = []
for i in date:
    dic_date[i] = 0
for k in dic_date:
     for i in range(data.shape[0]):            
        if str(data.iloc[i,3]) == str(k):            
            dic_date[k] = dic_date[k] + int(data.iloc[i,1])
     List_Traffic_All.append(dic_date[k])

Sum_All = 0 
for i in List_Traffic_All:
    Sum_All = Sum_All + i 


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
              ]), 
       
       
    dbc.Row([                       
            dbc.Col([html.Br(),
                 html.Div([html.Br(), html.Label('Percentage of Traffic in Regions'),
            dcc.Graph(id='pie_graph', config={'displayModeBar': False})
        ],style = {'border': '2px solid gray','border-radius':'15px','font-size':'140%',
                                       #'font-family': 'Roboto Condensed',
                                       'font-weight': 'bold',                                                                              
                                       'textAlign':'center'})],lg = 7)
                              
        
       ])
], style={'backgroundColor': '#eeeee'}) 


@app.callback(
    Output("pie_graph", "figure"),
    [Input('year_select', 'value')])

def pie_figure(year):
    
    Percent_C = Sum_Central*100/Sum_All
    Percent_W = Sum_Western*100/Sum_All
    Percent_E = Sum_Eastern*100/Sum_All
   
    Traffic_Region_pie = go.Pie(labels=["Central", "Western", "Eastern"], values=[round(Percent_C,2), round(Percent_W, 2), round(Percent_E,2)], marker=dict(colors=['#da202a', '#2a2a2d', '#c1c6c8']
                                                            , line=dict(color='#FFF', width=2)), 
                                                            domain={'x': [0.0, .7], 'y': [0.0, 1]}
                                                            , showlegend=True, name='Traffic in Regions', textinfo= 'label+value')
    layout = go.Layout(height = 700,
                   width = 800, 
                   autosize = True,
                   legend={"x": 0, "y": 0}
                                    
                   )
    fig = go.Figure(data = Traffic_Region_pie , layout = layout)
   
    return fig.to_dict()

    
    if __name__ == '__main__':
    app.run_server()

   
