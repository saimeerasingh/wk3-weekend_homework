from flask import render_template, request, redirect
from app import app
from models import items_list
from models.items_list import *
from models.items import *

@app.route('/items')
def index():
    return render_template('index.html', title = 'Shopping List',items_list=items_list)
    


