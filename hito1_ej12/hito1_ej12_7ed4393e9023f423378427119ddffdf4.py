#Juego adivina mi número
import random

numero = random.randint(1,20)
intentos = 0
Juego = True

while Juego:
   intentos += 1
   if intentos <= 5:
     Adivina = int(input("Ingrese el numero que quiere adivinar:"))
     if Adivina == numero:
      print("Adivinaste, mi numero era",numero)
      break
    
     elif Adivina > numero:
         print("mi numero es menor")
     elif Adivina < numero:
         print("mi numero es mayor")
         
     else:
        print("No adivinaste, mi numero era",numero)
        break