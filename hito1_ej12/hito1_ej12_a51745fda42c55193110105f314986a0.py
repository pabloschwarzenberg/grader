#Juego adivina mi número
import random as rd

numsec = rd.randint(1, 20)
intento = 0
adivina = False
while intento < 5:
   numero = int(input("Ingrese Numero a Adivinar "))

   if numero != numsec:
      intento += 1
      
      if numero < numsec:
         print("mi número es menor")
      
      if numero > numsec:
         print("mi número es mayor")

   else:
      adivina = True
      break

if adivina:
   print("Adivinaste, mi número era " + str(numsec))
else:
   print("No adivinaste, mi número era " + str(numsec))      