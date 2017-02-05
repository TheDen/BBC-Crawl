#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import scrapy
import requests
import html2text
import re
from urlparse import urlparse
import json
from newspaper import Article
from goose import Goose

g = Goose()
# for dispatcher
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals

class bbcspider(scrapy.Spider):
 name = "spider"
 allowed_domains = ["bbc.com"]
 start_urls = [
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

 def __init__(self):
   dispatcher.connect(self.spider_closed, signals.spider_closed)

 def spider_closed(self, spider):
  print "done"
  with open('output.json') as data_file:
    data = json.load(data_file)
    uniq = { each['url'] : each for each in data }.values()
  with open('output.json', 'w+') as out:
    json.dump(uniq, out)

 def parse(self, response):
  hrefs = response.css('::attr(href)').extract()
  paths = []
  for i in range(0, len(hrefs)):
   paths.append(urlparse(hrefs[i]).path)
  urls = []
  for i in paths:
   if i not in urls:
    urls.append(i)
  for i in range(0, len(urls)): 
     yield scrapy.Request(response.urljoin(urls[i]),
          callback=self.urlparse)

 def urlparse(self, response):

  match = re.search('[0-9]{8}',response.url)
  if match:

    url = response.url
    g = Goose()
    article = g.extract(url=url)

    yield {
     'headline': article.title,
     'url': url,
     'text': article.cleaned_text,
        } 
