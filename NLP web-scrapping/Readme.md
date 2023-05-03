# Web Scrapping 
- Web scrapping is actually web data extraction or web harvesting. It is the process of automatically extracting data from the websites. This is done by using software tools to crawl the web pages and extract the specific data fields such as texts, images and URLs. The extracted data can then be saved in a local file and databases for further analysis.

- Web scrapping can be done by using ,many programming languages such as `Python` `BeautifulSoup` `Scrapy`. The process typically involves sending HTTP request to a web server, parsing HTTP response and extracting desired data files.

## Load data from web
To load data from webpage using Python we can use the `urlib` or `requests module` 

```
import requests 
url="https://www.example.com"
response= requests.get(url)
print(response.txt)
```
`request.get() sends the HTTP get request to the speciified url`

## Process HTML page
- To process an HTML page using Python, we can use the BeautifulSoup module. BeautifulSoup is a Python library that provides tools for parsing and navigating HTML and XML documents
- Typical methods in BeautifulSoup -
`find()/find_all()` `get()` `text()` `contents()` `parent()` `siblings()`   

