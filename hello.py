from flask import Flask,request
import requests
from flask import jsonify
import os
import json
from flask import Flask,request

import time
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/create_client', methods=('GET', 'POST'))
def create_client():
    id = request.args.get('id')
    name = request.args.get('name')
    if(id == None or name == None):
        return 'Please give args as /create_client?id=<>&name=<>, '
    try:
        #r = requests.post("http://bugs.python.org",
        #                  data={'number': 12524, 'type': 'issue', 'action': 'show'})
        r = requests.post('http://localhost:3000/api/createClient',
            data = {"$class":"org.important.mynetwork.createClient",\
                     "name":name, 'id':id} ) 
        #print(r.status_code, r.reason)
    except:
        return jsonify({'status': 'Error','header':'error'})

    return jsonify({'status': r.status_code,'header':json.dumps(dict(r.content))})




@app.route('/create_bank', methods=('GET', 'POST'))
def create_bank():
    id = request.args.get('id')
    name = request.args.get('name')
    if(id == None or name == None):
        return 'Please give args as /api/timeseries/etf_data?ticker=<>, use /api/timeseries/etfs to find valid choices'
    try:
        #r = requests.post("http://bugs.python.org",
        #                  data={'number': 12524, 'type': 'issue', 'action': 'show'})
        r = requests.post('http://localhost:3000/api/createBank',
            data = {"$class":"org.important.mynetwork.createBank",\
                     "name":name, 'id':id} ) 
        #print(r.status_code, r.reason)
    except:
        return jsonify({'status': 'Error','header':'error'})

    return jsonify({'status': r.status_code,'header':json.dumps(dict(r.headers))})



@app.route('/create_verifier', methods=('GET', 'POST'))
def create_verifier():
    id = request.args.get('id')
    name = request.args.get('name')
    if(id == None or name == None):
        return 'Please give args as /api/timeseries/etf_data?ticker=<>, use /api/timeseries/etfs to find valid choices'
    try:
        #r = requests.post("http://bugs.python.org",
        #                  data={'number': 12524, 'type': 'issue', 'action': 'show'})
        r = requests.post('http://localhost:3000/api/createVerifier',
            data = {"$class":"org.important.mynetwork.createVerifier",\
                     "name":name, 'id':id} ) 
        #print(r.status_code, r.reason)
    except:
        return jsonify({'status': 'Error','header':'error'})

    return jsonify({'status': r.status_code,'header':json.dumps(dict(r.headers))})



@app.route('/get_bank', methods=('GET', 'POST'))
def get_bank():
    id = request.args.get('id')
    if(id == None):
        return jsonify({'status':'Error','header':'Please give args as /get_bank?id=<>'})
    
    try:
        r = requests.get('http://localhost:3000/api/Bank/{}'.format(id))

    except:
        return jsonify({'status': 'Error','header':'error'})
    
    return jsonify(json.loads(r.text ))


@app.route('/get_verifier', methods=('GET', 'POST'))
def get_verifier():
    id = request.args.get('id')
    if(id == None):
        return jsonify({'status':'Error','header':'Please give args as /get_verifier?id=<>'})
    
    try:
        r = requests.get('http://localhost:3000/api/Verifier/{}'.format(id))

    except:
        return jsonify({'status': 'Error','header':'error'})
    
    return jsonify(json.loads(r.text ))