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
	mongoimport -h $(HOST) -d $(DB) -c $(COLLECTION) -u $(USER) -p $(PASS) --file $(OUTPUTFILE) --jsonArray

test:
	./flaskr_tests.py

install:
	pip install -r requirements.txt
