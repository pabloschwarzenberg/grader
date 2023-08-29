import random
import sys
jugador=int(input("introduzca numero: "))
computador=random.randint(1,20)
for i in range(5):
    if jugador<computador:
        print("incorrecto, el numero indicado es menor")
        jugador=int(input("introduzca numero: "))
    elif jugador>computador:
        print("incorrecto, el  numero indicado es mayor")
        jugador=int(input("introduzca numero: "))
    elif jugador==computador:
        print("Adivinaste, mi numero era",computador)
        break
    if i==5:
      print("No adivinaste, mi numero era",computador)
      
if __name__ == "__main__":
    jugador=int(input("introduzca numero: "))
    