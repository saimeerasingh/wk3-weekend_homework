from flask import render_template, request, redirect
from app import app
from models import items_list
from models.items_list import *
from models.items import *

@app.route('/items')
def index():
    return render_template('index.html', title = 'Shopping List',items_list=items_list)
    
@app.route('/items',methods=['POST'])
def add_item():
    new_item_name = request.form['name']
    new_item_price = request.form['price']
    new_item_quantity = request.form['quantity']
    new_item_bought = True if 'bought' in request.form else False
    new_item_list = Items(new_item_name,new_item_price,new_item_quantity,new_item_bought)
    add_new_item(new_item_list)
    return redirect ('/items')

@app.route()