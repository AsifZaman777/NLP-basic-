import json
import pandas as pd
import textstat

with open('F:/NLP-basic-/exam solution/review.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

for review in df:
    number_of_words = len(review.split())
    
    num_sentences = len(review.split('.'))
    num_complex_words = textstat.lexicon_count(review, True)
    fk = textstat.flesch_kincaid_grade(review)
    
    fog_index = textstat.gunning_fog(review)
    
    coleman_liau_index = textstat.coleman_liau_index(review)
    smog_index = textstat.smog_index(review)
    
    auto_read_index = textstat.automated_readability_index(review)

    print(f"Total number of words: {number_of_words}")
    print(f"Total number of sentences: {num_sentences}")
    print(f"Total number of complex words: {num_complex_words}")
    print(f"Flesch-Kincaid Grade Level: {fk}")
    print(f"Gunning Fog Index: {fog_index}")
    print(f"Coleman-Liau Index: {coleman_liau_index}")
    print(f"SMOG Index: {smog_index}")
    print(f"Automated Readability Index: {auto_read_index}")
