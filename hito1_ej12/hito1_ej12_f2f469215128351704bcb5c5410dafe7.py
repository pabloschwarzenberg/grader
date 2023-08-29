#Juego adivina mi número
import random

intentos=0
numero=random.randint(1,20)
print('Bueno, piensa un número entre 1 y 20.')
while intentos<5:
  print ('¡Adivínalo! Tienes '+str(5 - intentos)+' intentos')
  adivina=int(input())


  if adivina<numero:
    print('mi número es mayor')

  elif adivina>numero:
    print('mi número es menor')

  else:
    intentos=5
  intentos=intentos+1

if adivina==numero:
    intentos=str(intentos)
    print('Adivinaste, mi número era ' +str(adivina))

if adivina!=numero:
    numero=str(numero)
    print('No adivinaste, mi número era '+numero) 