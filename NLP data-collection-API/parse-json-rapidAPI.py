import http.client
import json
import csv

conn = http.client.HTTPSConnection("yelp-reviews.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "4a50d8ccb9msh758a9c967668169p15ed70jsncdc0ed803e29",
    'X-RapidAPI-Host': "yelp-reviews.p.rapidapi.com"
}

conn.request("GET", "/business-reviews?business_id=pearls-deluxe-burgers-san-francisco-3&page=1&query=cheese&language=en&num_pages=1", headers=headers)

res = conn.getresponse()
data = res.read()

# parse the json data

json_data = json.loads(data, strict=False)

review_data=json_data['data']['reviews']

reviews= []

#fetch the required data from yelp reviews

for review in review_data:
    review ={
        'id':review['review_id'],
        'review_text':review['review_text'],
        'rating':review['review_rating'],
        'location': review['author_location'],
        'time_created':review['review_datetime_utc']
    }
    reviews.append(review)

#save the reviews in a excel file

with open('reviews.csv', mode='w', newline='') as csv_file:
    fieldnames = ['id', 'review_text', 'rating', 'location', 'time_created']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for review in reviews:
        writer.writerow(review)

