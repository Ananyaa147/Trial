from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/') 
def home():
    return render_template('Pleasework.html')

if __name__ == "__main__":
    app.run(debug=True)
