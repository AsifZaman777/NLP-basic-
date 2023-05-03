import requests


#fetch data from webpages
url='https://www.w3schools.com/html/html_styles.asp'
print("Text data \n\n",requests.get(url).text)


