import pyphen
dic= pyphen.Pyphen(lang='en_US')

word= 'syllable'

syllables= dic.inserted(word)
print(syllables)
print(len(syllables.split('-')))



