#Juego adivina mi número
import random
aleatorio=random.randint(1,20)

contador=1
jugador=int(input('Adivine el numero que se encuentra entre el 1 y el 20, tiene 5 intentos: '))
     
while contador!=5:
     if jugador>aleatorio:
          print('mi número es menor')
     if jugador<aleatorio:
          print('mi número es mayor')
     if jugador== aleatorio:
          print('Adivinaste, mi número era'+ str(aleatorio))
          break
     contador+=1
     jugador=int(input('intento numero '+ str(contador) + ':'))
     
if contador==5 and jugador == aleatorio:
     print('Adivinaste, mi número era' + str(aleatorio))
          
if jugador!=aleatorio:
     print('No adivinaste, mi número era'+ str(aleatorio))
     
