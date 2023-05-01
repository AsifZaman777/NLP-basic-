import string 
import pyphen
import numpy as np


dic=pyphen.Pyphen(lang='en_US')
punctuation= string.punctuation
print(punctuation)

random_string='s campus is located in an urban setting at Kuratoli, Khilkhet in Dhaka. The campus area is about 90 acres (36 ha). There is a total building area of 1,300,000 square feet (120,000 m2).[8][9] The university campus is considered as most beautifully designed compared to other private universities. AIUB places students, faculties & employees at its heart, creating an ideal green environment for continued creativity, innovation and wellbeing. The AIUB campus is open-architecture and connected to nature and the product of a remarkable collaboration. AIUB has 25 computer labs, 19 engineering labs, 10 design studios, 4 physics labs, 2 chemistry labs, and 1 language lab with 40 workstations in each and 24 servers to support the IT infrastructure. AIUB also has an International standard Moot Court to facilitate the overall clinical legal education. It also has State-of-the-art Auditorium and Multipurpose Hall, with built-in acoustics, world-class sound systems, P3 LED projection screens and a seating capacity of around 1000. There are various available facilities such as AIUB Daycare Facilities, Recreational Area, Cafeteria, student Lounge, etc. for students.'

print(random_string)

random_string=random_string.lower() #case sensitive

#eleminate the punctuations

for i in punctuation:
    if i in punctuation:
        random_string=random_string.replace(i, ' ')
print(random_string.split())


#NLP vocabulary can count all the recurrencies of words 

vocabs= {}

for i in random_string.split():
    if i in vocabs:
        vocabs[i] += 1
    else:
        vocabs[i] = 1

print(vocabs) 





