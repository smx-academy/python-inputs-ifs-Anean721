'''Da se napravi programa vo koja korisnikot ke vnese godina na ragjanje,
 ke se presmeta kolku godini e i da se odredi dali e maloleten ili polnoleten'''



x=(input('vnesete ime na korisnik'))
y=int(input('vnesete godina na ragjanje na korisnik'))
z= int(2022-y)


if z > 18:
        print('korisnikot e polnoleten i ima {} godini'.format(z))
else:
        print ('korisnikot e maloleten')
        
                