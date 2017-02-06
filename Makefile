#!/usr/bin/make -f

OUTPUTFILE=output.json
USER=
PASS=
DB=
COLLECTION=
SSLCERT=
HOST=
OUTPUTFILE=
run-spider:
	scrapy runspider spider.py --output=$(OUTPUTFILE)  

run-server:  
	# Creating new function...
	./apiserver.py

clean:
	# Deleting existing function...
	rm $(OUTPUTFILE)

db-import:
	mongoimport -u $(USER)- p $(PASS)--port 16943 --db $(DB) --collection $(COLLECTION) --ssl --sslCAFile $(SSLCERT) --host $(HOST) --file $(OUTPUTFILE) --jsonArray --drop --batchSize=1


install: 
	pip install -r requirements.txt
	pip install git+git://github.com/robmcdan/python-goose.git
