#Juego adivina mi número
import random

n = random.randint(1,20)
trys = 0
play = True

while play:
    trys += 1
    if trys <= 5:
        x = int(input("Ingrese un numero del 1 al 20: "))
        if x == n:
            print("Adivinaste, mi numero era: ",n)
            play = False
        elif x > n:
            print("mi numero es menor")
        elif x < n:
            print("mi numero es mayor")
    else:
        print("No adivinaste, mi número era: ",n)
        jugando = False
        break

     