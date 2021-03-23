from flask import Flask, request, render_template, jsonify, session
from forex_python.converter import CurrencyRates

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
    

    curr_one = request.form.get('cur1')

    return render_template("converter.html", curr_one=curr_one)