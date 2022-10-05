from flask import Flask, request
from dbhelpers import run_statement
import json

app = Flask(__name__)

@app.get('/api/clients')
def get_all_clients():
    results = run_statement("CALL get_all_clients()")
    if(type(results) == list):
        clients_json = json.dumps(results, default=str)
        return clients_json
    else:
        return "Sorry, something has gone wrong."


@app.get('/api/loyal_clients')
def get_clients_by_loyalty_points():
    min_points = request.args.get('min_points')
    results = run_statement("CALL get_clients_by_loyalty_points(?)", [min_points])
    if(type(results) == list):
        clients_json = json.dumps(results, default=str)
        return clients_json
    else:
        return "Sorry, something has gone wrong."

app.run(debug=True)