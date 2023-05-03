import requests


#fetch data from webpages
url_referance='https://www.w3schools.com/html/html_styles.asp'
print("Text data \n\n",requests.get(url_referance).text)


