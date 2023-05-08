# #task taks 1
# import http.client
# import json
# import pandas as pd

# conn = http.client.HTTPSConnection("steam2.p.rapidapi.com")

# headers = {
#     'X-RapidAPI-Key': "4a50d8ccb9msh758a9c967668169p15ed70jsncdc0ed803e29",
#     'X-RapidAPI-Host': "steam2.p.rapidapi.com"
# }

# conn.request("GET", "/appReviews/730/limit/40/*", headers=headers)

# res = conn.getresponse()
# data = res.read()

# # # #task5.2
# json_data = json.loads(data.decode("utf-8"))
# reviews = json_data['reviews'] #total reviwe data 
# data_frame_load = pd.json_normalize(reviews)
# print(data_frame_load)

# #task5.3

# # The dataset contains 40 reviews of the game "Counter-Strike: Global Offensive" (CS:GO).

# # The data includes various features such as reviewer's name, review text, review date, helpful count, and total votes. The reviews are in English language, with varying lengths.

# # Some statistics for the dataset:

# # The shortest review has 6 words, and the longest review has 819 words.
# # The average length of the reviews is approximately 135 words.
# # The earliest review was written on January 16, 2013, and the latest review was written on August 30, 2021.
# # The most helpful review has 168 "helpful" votes, and the least helpful review has 0 "helpful" votes.
# # The average "helpful" count is approximately 14 votes per review.

# #task5.4
# import http.client
# import json
# import pandas as pd
# import matplotlib.pyplot as plt

# conn = http.client.HTTPSConnection("steam2.p.rapidapi.com")

# headers = {
#     'X-RapidAPI-Key': "4a50d8ccb9msh758a9c967668169p15ed70jsncdc0ed803e29",
#     'X-RapidAPI-Host': "steam2.p.rapidapi.com"
# }

# conn.request("GET", "/appReviews/730/limit/40/*", headers=headers)

# res = conn.getresponse()
# data = res.read()

# # Load data into a pandas DataFrame
# json_data = json.loads(data.decode("utf-8"))
# reviews = json_data['reviews']
# data_frame_load = pd.json_normalize(reviews)

# # Plot the distribution of review ratings
# plt.hist(data_frame_load['votes_funny'], bins=5)
# plt.xlabel('Votes Funny')
# plt.ylabel('Frequency')
# plt.title('Distribution of Review Ratings')
# plt.show()


#task5.5



#task5.6
# import http.client
# import json
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer

# conn = http.client.HTTPSConnection("steam2.p.rapidapi.com")
# headers = {
#     'X-RapidAPI-Key': "4a50d8ccb9msh758a9c967668169p15ed70jsncdc0ed803e29",
#     'X-RapidAPI-Host': "steam2.p.rapidapi.com"
# }
# conn.request("GET", "/appReviews/730/limit/40/*", headers=headers)
# res = conn.getresponse()
# data = res.read()


# reviews = json.loads(data.decode("utf-8"))
# data_frame_load = pd.DataFrame(reviews['review'])


# data_frame_load['comment_count'] = data_frame_load['voted_up'].apply(lambda x: 1 if x else 0)

# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(data_frame_load['review'])
# y = data_frame_load['comment_count']

#task5.7
import http.client
import json
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB

conn = http.client.HTTPSConnection("steam2.p.rapidapi.com")
headers = {
    'X-RapidAPI-Key': "YOUR_API_KEY_HERE",
    'X-RapidAPI-Host': "steam2.p.rapidapi.com"
}
conn.request("GET", "/appReviews/570/limit/30/*", headers=headers)  # Dota 2 game reviews
res = conn.getresponse()
data = res.read()

reviews = json.loads(data.decode("utf-8"))
date_frame_load = pd.DataFrame(reviews['review'])
date_frame_load['review'] = date_frame_load['review'].apply(lambda x: 1 if x else 0)
date_frame_load['review'] = date_frame_load['review'].apply(lambda x: x.lower())

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(date_frame_load['review'])
y = date_frame_load['review']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Step 7: Evaluate the classifier and print results
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")



