import nltk
from nltk.stem import WordNetLemmatizer

lm=WordNetLemmatizer()

text_file=open('stem_words.txt','r')
random_text=text_file.read()
space=' '

for i in random_text:
    random_text=random_text.replace(space,' ')

words = random_text.split()

for w in words:
    print(w, ':' , lm.lemmatize(w))


#Output

# programmer : programmer
# is : is
# programming : programming
# to : to
# make : make
# the : the
# programs : program
# more : more
# programatically : programatically
# correct. : correct.
# Love : Love
# is : is
# a : a
# great : great
# thing : thing
# but : but
# ot : ot
# the : the
# best. : best.
# Good : Good
# best : best
# better : better
# are : are
# the : the
# three : three
# forms : form
# of : of
# good : good

