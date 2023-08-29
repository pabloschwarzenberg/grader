#Juego adivina mi número
import random
from random import randint
intentos=0
a=1
b=20
numero=random.randint(a,b)

print("adivina el numero que esta entre 1 y el 20")
print("tienes 5 intentos para adivinarlo")

while intentos <=4:
             adivina=input("ingresa el numero que creas que es: ")
             intentos=intentos+1
             adivina=int(adivina)

             if  adivina<numero:
                          print("mi número es mayor")

             if adivina >numero:
                          print("mi numero es menor")

             if adivina==numero:
                          print("Adivinaste, mi número era", numero)
                          break
if adivina !=numero:
             print("No adivinaste, mi número era", numero)
