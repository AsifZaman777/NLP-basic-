# The goal is to set emogi after the sentence on the basis of the sentiment intensity

import nltk
import string
import emoji
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

san=SentimentIntensityAnalyzer()

user_test_review="I have used xiomi phone. But the fact of unfortunate that it was the worst phone I ever seen. But I am quite good now after purchasing the apple Iphone 14 pro. So please dont purchase the shit"

user_test_review = user_test_review.split(".")

for s in user_test_review:
    s = s.strip()
    if s:
      if 'compound' in san.polarity_scores(s):
         if (san.polarity_scores(s)['compound'])<1:
            print(s+emoji.emojize(":dissapointed:"))
            


