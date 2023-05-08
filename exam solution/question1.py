import pandas as pd
import nltk
import json
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
nltk.download('punkt')

with open('F:/NLP-basic-/exam solution/review.json', 'r') as file:
    data = file.read()
json_data_print = json.loads(data)

print(json_data_print)
load_data_frame = pd.read_json('F:/NLP-basic-/exam solution/review.json')
print(load_data_frame.head())

#task 2a
#spell correction 
def correct_spelling(text):
    return text

corrected_review = correct_spelling(load_data_frame)
print('Corrected Review:', corrected_review)

#task 2b
for review in load_data_frame:
    tokens = nltk.word_tokenize(review)
    num_words = len(tokens)
    print(f"Total number of words in review: {num_words}")
print("\n")

#task 2c
sentece_count=0
for review in load_data_frame:
    sentences = review.split('.')

    for sentence in sentences:
        print(sentence.strip())
        sentece_count+=1
print("Sentense counts : ",sentece_count)
print("\n")

#task 2d
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer('english')

print("Stemmed words : ")
for review in load_data_frame:
    words = nltk.word_tokenize(review)

    stemmed_words = [stemmer.stem(word) for word in words]
    stemmed_sentence = ' '.join(stemmed_words)
    print(stemmed_sentence)
print("\n")

#task 2e
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
lemmatizer = WordNetLemmatizer()

for review in load_data_frame:
    sentences = sent_tokenize(review)

    for sentence in sentences:
        words = word_tokenize(sentence)
        lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
        print('lemmetized word : ')
        print(' '.join(lemmatized_words))



        




















