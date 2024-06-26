'''
------- Beispiel: Das built-in Modul random
'''

'''
random_value = random.randint(2, 7)
#beide zahlen sind im range inkludiert
print(random_value)
'''
'''
import random

lottery = ["Susi","Carsten","Dieter","Hans","Daniela"]
winner = random.choices(lottery, weights=[100,2,3,4,5], k=3)
# Sample: Einzigartige Objekte anzurufen
print(winner)
'''

import random
lottery = ["Susi","Carsten","Dieter","Hans","Daniela"]
print(lottery)
random.shuffle(lottery)
print(lottery)







