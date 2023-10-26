from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/api/truck/', methods=['GET'])
def get_trucks():
    trucks = [
        {'id': 1, 'year': 2016, 'make': 'Toyota', 'model': 'RAV4 Hybrid'},
        {'id': 2, 'year': 2018, 'make': 'Jeep', 'model': 'Grand Cherokee'},
        {'id': 3, 'year': 2021, 'make': 'Ford', 'model': 'Bronco'}  
    ]
    return jsonify(trucks)

@app.route('/api/truck-details/', methods=['GET'])
def find_truck():
    details = {'id': 3, 'year': 2021, 'make': 'Ford', 'model': 'Bronco'}  
    return (details)
  
@app.route('/api/locations/', methods=['GET'])
def find_locations():
    locations = { 'lat': 54.469458201384235,'lng': -6.3717700016563645 }
    return (locations)
