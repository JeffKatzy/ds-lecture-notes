import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1('hello world'),
    dcc.Graph(
        id = 'whatever',
        figure = {
            'data': [],
            'layout': {
                'title': 'something here'
            }
        }),
    dcc.Graph(
        id = 'ok',
        figure = {
            'data': [],
            'layout': {
                'title': 'something else'
            }
        }
    )
])

app.run_server(debug=True)
