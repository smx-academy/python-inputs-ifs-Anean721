'''Da se napravi programa vo koja korisnikot ke vnese 2 broevi 
i da se proveri dali zbirot e pomal od 100'''

x=int(input('vnesete prv broj'))
y=int(input('vnesete vtor broj'))
z=x+y

if z < 100 :
    print("zbirot {} e pomal od 100".format(z))
    print("uslovot e ispolnet")
else:
    print('zbirot {} e pogolem od 100'.format(z))

