from textblob import TextBlob

file=open('spelling.txt','r')
misspelled_string=file.read()

space=' '

for i in misspelled_string:
    misspelled_string=misspelled_string.replace(space, ' ')

words=misspelled_string.split()

#only the misspelled words are resolved

for w in words:
    blob=TextBlob(w)
    corrected=blob.correct()
    
    if w!=corrected:
       print(w, ":",corrected)
    
    

