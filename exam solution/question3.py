import pandas as pd
import string

data_frame_load = pd.read_csv('F:/NLP-basic-/exam solution/amazon_review.csv')

data_frame_load.drop_duplicates(inplace=True)
data_frame_load.dropna(inplace=True)
data_frame_load['weight'] = str(data_frame_load['weight']).lower()
data_frame_load['weight'] = str(data_frame_load['weight']).replace('[^\w\s]','')

print(data_frame_load)


