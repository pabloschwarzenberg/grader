#Juego adivina mi número
import random

intentos = 0

x = random.randint (1, 20)

while intentos < 5:
   intentos = intentos + 1
   numero = int(input("Elige un numero del 1 al 20: "))
   if numero < x:
      print ("mi número es mayor")
   if numero > x:
      print ("mi número es menor")
   if numero == x:
      break

if numero == x:
   print ("Adivinaste, mi número era ",x)

if numero != x:
   print ("No adivinaste, mi número era ",x)     
        
     