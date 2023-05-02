import nltk
from nltk import PorterStemmer


ps= PorterStemmer()

text_file=open('stem_words.txt','r')

random_string= text_file.read()
space=' '
for i in random_string:
    random_string=random_string.replace(space,' ')

words= random_string.split()

# implement the nltk to turn the words into their base form 

for w in words:
    print(w ,':', ps.stem(w))

## Output

# programmer : programm
# is : is
# programming : program
# to : to
# make : make
# the : the
# programs : program
# more : more
# programatically : programat
# correct : correct



