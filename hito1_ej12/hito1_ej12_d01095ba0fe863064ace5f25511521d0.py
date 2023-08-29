#Juego adivina mi número
import random
numero=random.randint(1,20)
juegos=5
while juegos>0:
   numero_jugador=int(input())
   if numero_jugador<numero:
        print("mi numero es mayor")
   elif numero_jugador>numero:
        print("mi numero es menor")     
   juegos=juegos-1
if numero_jugador==numero:
   print("Adivinaste, mi numero era",numero)
else:
   print("No adivinaste, mi numero era",numero)
