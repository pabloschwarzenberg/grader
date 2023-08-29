#MAQUINA DE VUELTO

import math
import random
print()
print()
print('%%%%%%%% EJERCICIO CLASE 11 AGOSTO %%%%%%%%%')
print()
print('Definamos una recta L1: a1x + b1x = c1 con coeficientes en R')
#defino coeficientes a usar
print()
a1=int(input('ingresa un valor para a1:  '))
b1= int(input('Y otro valor para b1:  '))
c1= int(input('Ingresa el valor libre de la primera recta:  '))
print()
print()
print('Ya tienes definida una recta, vamos por L2')
print()
print()
a2=int(input('ingresa un valor para a2:  '))
b2= int(input('Y otro valor para b2:  '))
c2= int(input('Ingresa el valor libre de la segunda recta:  '))
#usando krammer
den=a1*b2-b1*a2
#resultado de variables
parx=(c1*b2-c2*b1)/den
pary=(a1*c2-c1*a2)/den
print("['x={}','y={}']".format(parx,pary))



