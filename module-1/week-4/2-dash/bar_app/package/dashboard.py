import dash_core_components as dcc
import dash_html_components as html
from package import app
from package.routes import customer_orders_trace

orders_trace = customer_orders_trace()

app.layout = html.Div(children=[
    html.H1('hello world'),
    dcc.Graph(
        id = "uber_pricing_graph",
        figure = {
            'data': [orders_trace],
            'layout': {
                'title': 'Uber Pricing in Brooklyn and Manhattan'
            }
        }
    )
])
