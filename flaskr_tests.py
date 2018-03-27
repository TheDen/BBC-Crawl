#!/usr/bin/env python
from flask import Flask
import unittest
import flask_testing
from flask import request
import requests

class FlaskrTestCase(unittest.TestCase):

 def testroot(self):
   url = "http://127.0.0.1:5000"
   print url
   res = requests.request('GET', url)
   self.assertEqual(res.status_code, 200)

 def testquery(self):
   url = "http://127.0.0.1:5000/api/v1/articles/?query=a"
   print url
   res = requests.request('GET', url)
   self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
  unittest.main()
