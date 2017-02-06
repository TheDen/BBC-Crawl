#!/usr/bin/make -f

OUTPUTFILE=output.json

run-spider:
	scrapy runspider spider.py --output=$(OUTPUTFILE)  

run-server:  
	# Creating new function...
	./apiserver.py

clean:
	# Deleting existing function...
	rm $(OUTPUTFILE)

install: 
	pip install -r requirements.txt
	pip install git+git://github.com/robmcdan/python-goose.git
