# scrape

Scrapes articles from www.bbc.com using `scrapy`, and creates an api using `flask` to query the articles for keywords.

Live version: 104.236.85.149

Example query: 104.236.85.149/api/v1/articles/?query=sydney


### Build
Requirements:

`mongo`: https://docs.mongodb.com/getting-started/shell/installation/

`pip`: `wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py`

Pip modules (`make install` should also install these)
```
pip install -r requirements.txt
pip install git+git://github.com/robmcdan/python-goose.git
```
Ubuntu might need certain prereqs:
```
sudo apt-get update
sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
```
### Run
To run the spider:

`make run-spider`

To start the server:

`make run-server`

To import the db to compose:

`db-import`

### API

Once the server is running, for example a query for the word `sydney` on bbc.com can be made at the enpoint:

`104.236.85.149/api/v1/articles/?query=sydney`


