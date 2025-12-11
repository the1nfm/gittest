print('hello world')
from flask import Flask, render_template, request, redirect, url_for
import os
import json
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return render_template('success.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True) # Run the Flask app in debug mode