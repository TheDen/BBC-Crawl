#!/usr/bin/env python
# -*- coding: utf-8 -*-
import flask
from flask import Flask, request, jsonify
from flask_restful import Resource
import json
from bson.objectid import ObjectId
from pymongo import MongoClient
import os
import sys
import ssl
from flask import render_template
# grab creds from the env var
MONGODB_URL = os.environ.get('MONGODB_URL')
# load client with ssl certificate

try:
  client = MongoClient(MONGODB_URL)
except:
  print "err: can't connect to db. Make sure MONGODB_URL is set"
  sys.exit()

# check db collecion, load it into memory
db = client.bbc
collection = db.data
try:
  data = list(collection.find())
except:
  print "err: can't find collection on db"
  sys.exit()

app = Flask(__name__)

# handle 404s
@app.errorhandler(404)
def page_not_found(e):
  return flask.jsonify(error=404, text=str(e)), 404

@app.route("/")
def base_url():
    return flask.make_response("/api/v1/articles/?query=example", 200)

@app.route('/api/v1/articles/')
def get_matches():
   query = request.args.get('query')
   if not query:
     return flask.jsonify(error=404, text="empty query"), 404

   objectid = []
   j = 0
   # look for can insensitive search text in headline and article
   for i in data:
    if query.lower() in i.values()[0].lower() or query.lower() in i.values()[3].lower():
     objectid.append(j)
    j += 1

   if len(objectid) == 0:
     return flask.jsonify(error=404, text="no match"), 200
   resp = []
   for i in objectid:
    resp.append(json.dumps({'url': data[i].values()[1] , 'headline': data[i].values()[0], 'article': data[i].values()[3] }))

   # fix string to make it valid json
   response_str = json.dumps(resp, sort_keys=False, separators=(',', ':')).replace('["','[').replace('"]',']').replace("\\\"", "\"").replace("\\\\\"", "\\\"").replace("}\"", "}").replace("\"{", "{")
   response = flask.make_response(response_str, 200)
   response.headers['Content-Type'] = 'application/json'
   return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
