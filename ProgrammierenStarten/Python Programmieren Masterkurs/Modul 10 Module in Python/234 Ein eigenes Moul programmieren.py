'''
------- 2. Ein eigenes Modul programmieren
------- 3. Module einbinden/laden
'''

#import ZDCalc as calculation
from ZDCalc import faculty, addition

def addition(a,b):
    return a - b

#from ZDCalc import faculty, addition
import ZDCalc

res = addition(5,10)
print(res)

res2 = faculty(5) #1*2*3*4*5
print(res2)









