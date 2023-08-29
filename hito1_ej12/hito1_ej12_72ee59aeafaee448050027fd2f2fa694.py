#Juego adivina mi número
import random
juegos=5
numero_computador=int(random.randint(1,20))
while juegos>0:
    numero_jugador=int(input("en que numero pensé?: "))
    if numero_jugador<numero_computador:
      print("mi numero es mayor")
    elif numero_jugador>numero_computador:
      print("mi numero es menor")
    else:
      print("Advinaste, mi numero era",numero_computador)
      break
    juegos=juegos-1
print("No adivinaste, mi numero era",numero_computador)

   