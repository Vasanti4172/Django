import dash  
from dash import html, dcc  


my_app = dash.Dash(__name__)  

my_app.layout = html.Div([
    html.H1(" Creating My First Dash App"),
    dcc.Input(placeholder='Please enter your text...')
])


if __name__ == '__main__':  
    my_app.run_server(debug=True) 
