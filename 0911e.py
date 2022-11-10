'''Da se napravi programa vo koja korisnikot 
ke vnese nekoe ime i da se proveri sekoga samoglaska kolku pati
 se pojavuva vo ime i od kolku karakteri e sostaveno toa ime'''

samoglaski='aeiou'
x=input("Vnesete go Vaseto ime")
count ={}.fromkeys(samoglaski,0)
for karakter in x:
    if karakter in count:
        count[karakter]+=1
karakter=(len(x))
print(count)
print('Vaseto ime e sostaveno od karakteri: ', karakter)