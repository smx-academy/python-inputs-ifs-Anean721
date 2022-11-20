'''Da se napravi programa vo koja korisnikot ke vnese goleminite na aglite 
na triagolnici, i da se proveri dali so tie golemini 
moze da se kreira triagolnik(zbirot treba da bide 180)'''



x=int(input('vnesete prv agol na triagolnik'))
y=int(input('vnesete vtor agol na triagolnik'))
z=int(input('vnesete tret agol na triagolnik'))
zbir=x+y+z
if zbir<=180:
    print('moze da se kreira takov triagolnik')
else:
    print('proverkata na zbirot na agli pokazuva deka ne moze da se kreira triagolnik')
    