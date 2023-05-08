import http.client
import json
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB

# Step 1: Fetch review data from RapidAPI
conn = http.client.HTTPSConnection("steam2.p.rapidapi.com")
headers = {
    'X-RapidAPI-Key': "YOUR_API_KEY_HERE",
    'X-RapidAPI-Host': "steam2.p.rapidapi.com"
}
conn.request("GET", "/appReviews/570/limit/30/*", headers=headers)  # Dota 2 game reviews
res = conn.getresponse()
data = res.read()

# Step 2: Load and preprocess the data
reviews = json.loads(data.decode("utf-8"))
df = pd.DataFrame(reviews['reviews'])
df['sentiment'] = df['voted_up'].apply(lambda x: 1 if x else 0)
df['review'] = df['review'].apply(lambda x: x.lower())

# Step 3: Summarize the data
print("Data Summary:")
print("--------------")
print(f"Number of reviews: {len(df)}")
print(f"Number of positive reviews: {df['sentiment'].sum()}")
print(f"Number of negative reviews: {len(df) - df['sentiment'].sum()}")
print(f"Average review length: {df['review'].apply(len).mean():.2f} characters")

# Step 4: Visualize the data
df['sentiment'].value_counts().plot(kind='bar')
plt.title("Distribution of Review Sentiments")
plt.xlabel("Sentiment (0=negative, 1=positive)")
plt.ylabel("Number of Reviews")
plt.show()

# Step 5: Vectorize the review text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['review'])
y = df['sentiment']

# Step 6: Split the data and train a classifier
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Step 7: Evaluate the classifier and print results
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
