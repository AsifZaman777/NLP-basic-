import string 
import pyphen

dic=pyphen.Pyphen(lang='en_US')
punctuation= string.punctuation
print(punctuation)

random_string= 'This is a string to check the process! yes it? "works" '

# returning the syllable basis
print(dic.inserted(random_string).split('-'))

##split the whole string wihtout taking the punctuation

for i in punctuation:
    random_string=random_string.replace(i, ' ')

print(random_string.split())