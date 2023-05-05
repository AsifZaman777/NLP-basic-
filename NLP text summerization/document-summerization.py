# we need to find the complex words in a particular text
# Count the complex words in the text

import nltk
import string
from nltk.corpus import words

nltk.download('words')
nltk.download('cmudict')
nltk.download('punkt')
english_words=set(words.words())


text="The university's campus is located in an urban setting at Kuratoli, Khilkhet in Dhaka. The campus area is about 90 acres (36 ha). There is a total building area of 1,300,000 square feet (120,000 m2).[8][9] The university campus is considered as most beautifully designed compared to other private universities. AIUB places students, faculties & employees at its heart, creating an ideal green environment for continued creativity, innovation and wellbeing. The AIUB campus is open-architecture and connected to nature and the product of a remarkable collaboration. AIUB has 25 computer labs, 19 engineering labs, 10 design studios, 4 physics labs, 2 chemistry labs, and 1 language lab with 40 workstations in each and 24 servers to support the IT infrastructure. AIUB also has an International standard Moot Court to facilitate the overall clinical legal education. It also has State-of-the-art Auditorium and Multipurpose Hall, with built-in acoustics, world-class sound systems, P3 LED projection screens and a seating capacity of around 1000. There are various available facilities such as AIUB Daycare Facilities, Recreational Area, Cafeteria, student Lounge, etc. for students."

punctuation=string.punctuation
number= '0123456789'

#remove punctuations and the numbers from the text

for i in punctuation:
    if i in text:
        text=text.replace(i,' ')

for i in number:
    if i in text:
        text=text.replace(i,' ')


tokens=nltk.word_tokenize(text)

token_update=[]

for token in tokens:
    token=token.lower()
    token_update.append(token)

print(token_update)
    
#initialize the complex word counter 
complex_words=0




