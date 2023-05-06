# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.metrics import accuracy_score, precision_score, confusion_matrix
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt

# # Task 1: Load and preprocess subjectivity.csv
# subjectivity_df = pd.read_csv('F:/NLP-basic-/exam solution/subjectivity.csv', header=None, names=['text', 'label'])
# subjectivity_df['label'] = subjectivity_df['label'].apply(lambda x: 1 if x == 'subj' else 0)

# # Task 2: Vectorize X and split the data
# tfidf = TfidfVectorizer()
# X = tfidf.fit_transform(subjectivity_df['text'])
# y = subjectivity_df['label']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# # Task 3: Train and evaluate the model
# clf = MultinomialNB()
# clf.fit(X_train, y_train)
# y_pred = clf.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# precision = precision_score(y_test, y_pred)
# conf_matrix = confusion_matrix(y_test, y_pred)
# print('Accuracy:', accuracy)
# print('Precision:', precision)
# print('Confusion matrix:\n', conf_matrix)

# # Task 4: Load and preprocess amazon_review.csv
# amazon_df = pd.read_csv('F:/NLP-basic-/exam solution/amazon_review.csv', header=None, names=['text'])
# amazon_df['text'] = amazon_df['text'].apply(lambda x: x.lower())

# # Task 5: Loop over reviews and classify them
# for i, review in enumerate(amazon_df['text']):
#     review_vec = tfidf.transform([review])
#     prediction = clf.predict(review_vec)[0]
#     print(f'Review {i + 1}: {review}')
#     print('Classification:', 'Subjective' if prediction == 1 else 'Objective')

# # Task 6: Calculate accuracy, precision, and confusion matrix for amazon_review.csv
# amazon_X = tfidf.transform(amazon_df['text'])
# amazon_y = clf.predict(amazon_X)
# amazon_accuracy = accuracy_score(y, amazon_y)
# amazon_precision = precision_score(y, amazon_y)
# amazon_conf_matrix = confusion_matrix(y, amazon_y)
# print('Amazon Review Accuracy:', amazon_accuracy)
# print('Amazon Review Precision:', amazon_precision)
# print('Amazon Review Confusion matrix:\n', amazon_conf_matrix)

# # Task 7: Split subjectivity.csv into subjective and objective datasets
# subjective_df = subjectivity_df[subjectivity_df['label'] == 1]
# objective_df = subjectivity_df[subjectivity_df['label'] == 0]

# # Task 8: Plot word clouds for subjective and objective datasets
# subjective_text = ' '.join(subjective_df['text'])
# objective_text = ' '.join(objective_df['text'])
# subjective_cloud = WordCloud().generate(subjective_text)
# objective_cloud = WordCloud().generate(objective_text)

# # Task 9: Interpret the word clouds
# plt.subplot(1, 2, 1)
# plt.imshow(subjective_cloud, interpolation='bilinear')
# plt.title('Subjective')
# plt.axis('off')

# plt.subplot(1, 2, 2)
# plt.imshow(objective_cloud, interpolation='bilinear')
# plt.title('Objective')
# plt.axis('off')
# plt.show()
