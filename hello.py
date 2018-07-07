from flask import Flask,request
import requests
from flask import jsonify
import os
import json
from flask import Flask,request

import time
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS (app)


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
        return 'Please give args as /create_bank?id=<>&name=<>, '
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
        return 'Please give args as /create_verifier?id=<>&name=<>,'
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


@app.route('/get_client', methods=('GET', 'POST'))
def get_clien():
    id = request.args.get('id')
    if(id == None):
        return jsonify({'status':'Error','header':'Please give args as /get_bank?id=<>'})
    
    try:
        r = requests.get('http://localhost:3000/api/Client/{}'.format(id))

    except:
        return jsonify({'status': 'Error','header':'error'})
    
    return jsonify(json.loads(r.text ))


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


@app.route('/verificationComplete', methods=('GET', 'POST'))
def verificDone():
    verID = request.args.get('verID')
    docID = request.args.get('docID')
    status = request.args.get('status')
    if(verID == None or docID == None or status == None):
        return jsonify({'status':'Error','header':'Please give args as /verificationComplete?verID=<>&docID=<>&status=<>'})

    try:
        r = requests.post('http://localhost:3000/api/verificationComplete',
                {  "$class": "org.important.mynetwork.verificationComplete",
                        "documentID": docID,
                                "verifierID": verID,
                                            "status": status,
                 } )
    except:
        return jsonify({'status': 'Error','header':'error'})

    return jsonify(json.loads(r.text))


@app.route('/clientALlowBank', methods=('GET', 'POST'))
def cab():
    docID = request.args.get('docID')
    bankID = request.args.get('bankID')
    if(docID == None or bankID == None):
        return jsonify({'status':'Error','header':'Please give args as /clientALlowBank?docID=<>&bankID=<>'})

    try :

        r = requests.post('http://localhost:3000/api/clientAllowsBank',
            {
                "$class": "org.important.mynetwork.clientAllowsBank",
                    "documentID": docID,
                        "bankID": bankID,  
            })

    except :
        return  jsonify({'status': 'Error','header':'error'})

    return jsonify(json.loads(r.text))





    




