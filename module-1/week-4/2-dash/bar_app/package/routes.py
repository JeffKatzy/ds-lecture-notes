import pdb
from package.models import *
from package import server
from package.plotly import trace_values

@server.route('/')
def show():
    customer = Customer.query.get(1)
    return customer.name

def customer_orders_trace():
    customers = Customer.query.all()
    customer_names = [customer.name for customer in customers]
    customer_orders = [customer.orders.count() for customer in customers]
    orders_trace = trace_values(customer_names, customer_orders, type='bar')
    return orders_trace
