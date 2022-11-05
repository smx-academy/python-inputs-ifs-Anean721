'''Da se napravi programa vo koja korisnikot ke vnese strani na dva pravoagolnici,
 da se presmeta plostinata i da se proveri koj pravoagolnik e pogolem'''

a1=int(input('vnesete strana a1 na pravoagolnik'))
b1=int(input('vnesete strana b1 na pravoagolnik'))
plostina1=a1*b1
print(plostina1)
a2=int(input('vnesete strana a2 na pravoagolnik'))
b2=int(input('vnesete strana b2 na pravoagolnik'))
plostina2=a2*b2
print(plostina2)
if plostina1 > plostina2:
    print('plostinata {} cm2 na prviot pravoagolnik e pogolema od plostinata {}cm2 na vtoriot pravoagolnik'.format(plostina1,plostina2))
    
   
else:
    print('plostinata {} cm2 na prviot pravoagolnik e pomala od plostinata {} cm2 na vtoriot pravoagolnik'.format(plostina1,plostina2))
      
      