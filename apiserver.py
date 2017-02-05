#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import flask
from flask import Flask, request
from flask_restful import Resource, Api
import json
from bson.objectid import ObjectId
from pymongo import MongoClient
import os
import ssl

MONGODB_URL = os.environ.get('MONGODB_URL')
client = MongoClient(MONGODB_URL,ssl_ca_certs="./sslfile.cert")
db = client.admin
collection = db.bbcdata
app = Flask(__name__)

#data = list(collection.find())

from flask import render_template

@app.errorhandler(404)
def page_not_found(e):
    return flask.make_response("page not founditry. Try /api/v1/?query=yourquery", 404)
@app.route("/")
def hello():
    return "hit /api/v1/?query=yourquery"

@app.route('/api/v1/')
def show_user_profile():
   query = request.args.get('query')

   if not query:
    return flask.make_response("need nonempty query parameter", 200)
   
   objectid = []
   j = 0
   for i in data:
    if query.lower() in i.values()[3].lower():
     print j
     objectid.append(j)
    j += 1

   if len(objectid) == 0:
     return flask.make_response("no match", 200)
   resp = []
   for i in objectid:
    match = data
    resp.append(json.dumps({'url': match[i].values()[1] , 'headline': match[i].values()[0], 'article': match[i].values()[3] }))
    
   response_str = json.dumps(resp, sort_keys=False, separators=(',', ':')).replace('["','[').replace('"]',']').replace("\\\"", "\"").replace("\\\\\"", "\\\"").replace("}\"", "}").replace("\"{", "{")
   response = flask.make_response(response_str, 200)
   response.headers['Content-Type'] = 'application/json'
   return response
  
if __name__ == "__main__":
    app.run()
