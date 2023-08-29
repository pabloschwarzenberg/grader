#Juego adivina mi número
from random import randint
from time import sleep

while True:
  numero = int(input('ingrese un numero'))
  secreto = randint(1,20)
  if numero == secreto:
    sleep(1)
    print('Adivinaste, mi número era ', secreto)
    
 if numero != secreto:
   if numero > secreto:
     print('mi número es menor')
   if numero < secreto:
     print('mi número es mayor')
   print('Intento numero 2')
   sleep(1)
   numero = int(input('ingrese un número'))
   if numero != secreto:
     if numero > secreto:
       print('mi número es menor')
     if numero <  secreto:
       print('mi número es mayor')
     print('Intento numero 3')
     sleep(1)
     numero = int(input('ingrese un número'))
     if numero != secreto:
       if numero > secreto:
         print('mi numero es menor')
       if numero < secreto:
         print('mi número es mayor')
       print('Intento numero 4')
       sleep(1)
       numero = int(input('ingrese un numero'))
       if numero != secreto:
         if numero > secreto:
           print('mi número es menor')
         if numero < secreto: 
           print('mi número es mayor')
         print('Intento numero 5')
         print('No adivinaste, mi número era', secreto)
         sleep(1)
         break
   