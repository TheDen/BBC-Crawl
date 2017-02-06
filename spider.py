#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import scrapy
import requests
import re
from urlparse import urlparse
import json
from goose import Goose
from scrapy import signals
import argparse
import sys

class bbcspider(scrapy.Spider):
 name = "spider"
 allowed_domains = ["bbc.com"]
 def __init__(self,*args, **kwargs):
   super(bbcspider, self).__init__(*args, **kwargs)
   start_urls = []
   urlargs = kwargs.get('start_urls')
   if not urlargs:
     #default urls
     self.start_urls = [
         'http://www.bbc.com',
         'http://www.bbc.com/news/',
         'http://www.bbc.com/news/world',
         'http://www.bbc.com/news/world/asia',
         'http://www.bbc.com/sport/',
         'http://www.bbc.com/travel/',
         'http://www.bbc.com/capital/',
         'http://www.bbc.com/culture/',
         'http://www.bbc.com/future/',
         'http://www.bbc.com/earth/uk',
         ]
   else:
     self.start_urls = kwargs.get('start_urls').split(',')

 def closed(self, response):
  # grab the --output arg
  try:
    outputfile =  filter(re.compile("--output=").match, sys.argv)[0].split("--output=")[1]
  except:
   print "err: can't open file"
   return
  if not outputfile:
    print "err: output file empty"
    return
  with open(outputfile) as data_file:
    try:
      data = json.load(data_file)
    except:
      print "err: can't parse" + outputfile
      return
    uniq = { each['url'] : each for each in data }.values()
  with open(outputfile, 'w+') as out:
    try:
      json.dump(uniq, out)
    except:
      print "err: can't write file"

 def parse(self, response):
  hrefs = response.css('::attr(href)').extract()
  paths = []
  for i in range(0, len(hrefs)):
   paths.append(urlparse(hrefs[i]).path)
  # remove duplicates
  urls = []
  for i in paths:
   if i not in urls:
    urls.append(i)
  for i in range(0, len(urls)):
     yield scrapy.Request(response.urljoin(urls[i]),
          callback=self.urlparse)

 def urlparse(self, response):
  # bbc.com articles have 8 digits in the url
  match = re.search('[0-9]{8}',response.url)
  if match:
    url = response.url
    article = Goose().extract(url=url)

    # JSON output data
    yield {
     'headline': article.title,
     'url': url,
     'text': article.cleaned_text,
        }
