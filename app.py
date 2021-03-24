from flask import Flask, request, render_template, jsonify, session
from forex_python.converter import CurrencyRates
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = "forex"
app.debug = True



@app.route('/')
def index():

    c = CurrencyRates()
    print(c.get_rates('USD'))
    return render_template("index.html")

@app.route('/converter', methods=['POST'])
def curr_converter():
    
    c = CurrencyRates()
    curr_one = request.form.get('cur1')
    curr_two = request.form.get('cur2')
    amount = request.form.get('value')
    print(curr_one)
    converted = c.convert(curr_one.upper(), curr_two.upper(), float(amount)) 
    print(converted)

    return render_template("converter.html", curr_one=curr_one, curr_two=curr_two, converted=converted)