# BBC-Crawl

Scrapes articles from www.bbc.com using `scrapy`, and creates an api using `flask` to query the articles for keywords.

Live version: https://bbc-crawl.herokuapp.com/

Example query: https://bbc-crawl.herokuapp.com/api/v1/articles/?query=sydney


### Build
Requirements:

`mongo`: https://docs.mongodb.com/getting-started/shell/installation/

`pip`: `wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py`

Pip modules (`make install` should also install these)
```
pip install -r requirements.txt
```

Ubuntu might need certain prereqs:
```
sudo apt-get update
sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
```

### Test: 

For a very simple test on localhost: `./flaskr_tests.py`

### Run

`MONGODB_URL` needs to be exported to connect to the mlab db:

`export MONGODB_URL=mongodb://$user:$pass@$db.mlab.com:$port/bbc`

To run the spider:

`make run-spider`

To start the server:

`make run-server`

To import the output file to a remote db:

`db-import`

### API

Once the server is running, for example a query for the word `sydney` on bbc.com can be made at the enpoint:

https://bbc-crawl.herokuapp.com/api/v1/articles/?query=sydney