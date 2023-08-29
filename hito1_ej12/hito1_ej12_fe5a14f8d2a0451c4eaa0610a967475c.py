#Juego adivina mi número
from random import *

nm=randint(1,20)

print('Intenta adivinar mi numero')
intento=5
while(intento>0):
  adv=int(input('Que numero crees que es?: '))
  if adv>nm:
    print('Mi numero es menor')
    intento-=1

  if adv<nm:
    print('Mi numero es mayor')	
    intento-=1

  if adv==nm:
    break
if intento>0:
  print('Adivinaste!')
if intento==0:
  print('No adivinaste, mi numero era ',nm)     