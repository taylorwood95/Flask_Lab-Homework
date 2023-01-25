from flask import render_template
from app import app
from models.order import Order
from models.order_list import orders


@app.route("/orders")
def index():
    return render_template("index.html", title="Home", orders=orders)


@app.route("/orders/<index>")
def one_order(index):
    one_order = orders[int(index)]
    return render_template("one_order.html", title="Home", orders=one_order)


@app.route("/orders/<index>")
def one_order(index):
    order = orders[int(index)]
    return render_template("one_order.html", title="Home", orders=order)