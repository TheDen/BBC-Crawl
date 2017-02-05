#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import flask
from flask import Flask, request
from flask_restful import Resource, Api
import json
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient()
db = client.test
collection = db.bbcdw6

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/api/v1/')
def show_user_profile():
   query = request.args.get('query')
   print query

   if not query:
    return flask.make_response("need nonempty query parameter", 200)

   data = list(db.bbcdw6.find())
   
   objectid = []
   
   for i in data:
    if query.lower() in i.values()[3].lower():
      objectid.append(i.values()[2])
      
    if len(objectid) == 0:
#      return flask.make_response("no match", 200)
      
    resp = []
    for i in range(0,len(objectid)):
     match = db.bbcdw4.find_one({'_id': ObjectId(objectid[i])})
     resp.append(json.dumps({'url': match.values()[1] , 'headline': match.values()[0], 'article': match.values()[3] }))
    
    response_str = json.dumps(resp, sort_keys=False, separators=(',', ':')).replace('["','[').replace('"]',']').replace("\\\"", "\"").replace("\\\\\"", "\\\"").replace("}\"", "}").replace("\"{", "{")
    response = flask.make_response(response_str, 200)
    response.headers['Content-Type'] = 'application/json'
    return response
  
if __name__ == "__main__":
    app.run()
    app.run()
