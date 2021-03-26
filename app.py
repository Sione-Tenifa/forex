from flask import Flask, request, render_template, jsonify, session, flash, redirect
from forex_python.converter import CurrencyRates
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = "forex"
app.debug = True



@app.route('/')
def index():

    c = CurrencyRates()
    print(c.get_rate)
    return render_template("index.html")

@app.route('/converter', methods=['POST'])
def curr_converter():
    
    c = CurrencyRates()
    Currency_list = c.get_rates('USD')

    curr_one = request.form.get('cur1')
    curr_two = request.form.get('cur2')
    value = float(request.form.get('value'))
    
    if Currency_list.keys() >= {curr_one.upper(), curr_two.upper()} and type(value) == float:

        print('in if')
        converted = c.convert(curr_one.upper(), curr_two.upper(), value) 
        new_converted = float("{:.2f}".format(converted))
        return render_template("converter.html", new_converted=new_converted)

    else:
        print(type(value))
        flash("Invalid currency or value")
        flash("Please make sure inputs are valid")

        return redirect("/")
    
