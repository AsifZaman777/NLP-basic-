import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from transformers import pipeline

# Load the Amazon review data
df = pd.read_csv("F:/NLP-basic-/exam solution/amazon_review.csv")

sentiment_analyzer = SentimentIntensityAnalyzer()
nlp = pipeline("summarization")

# Loop over the reviews
for index, row in df.iterrows():
    review = row["review"]

    # Generate review summary
    summary = nlp(review, max_length=100, min_length=2, do_sample=False)[0]["summary_text"]

    # Perform sentiment analysis
    sentiment_scores = sentiment_analyzer.polarity_scores(review)
    sentiment = ""
    if sentiment_scores["compound"] >= 0.05:
        sentiment = "Positive"
    elif sentiment_scores["compound"] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Compare sentiment analysis with review rating
    rating = row["rating"]
    if (sentiment == "Positive" and rating >= 4) or (sentiment == "Negative" and rating <= 2):
        correlation = "Strong"
    elif (sentiment == "Positive" and rating >= 3) or (sentiment == "Negative" and rating <= 3):
        correlation = "Moderate"
    else:
        correlation = "Weak"

    # Print review summary and sentiment analysis result
    print("Review Summary: ", summary)
    print("Sentiment Analysis Result: ", sentiment)
    print("Rating-Sentiment Correlation: ", correlation)
    print("==================================================")
