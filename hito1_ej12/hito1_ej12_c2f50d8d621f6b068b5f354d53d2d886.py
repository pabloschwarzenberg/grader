#Juego adivina mi número
      
import random

num = random.randint(1, 20)

correcto = False
intentos = 5
while not correcto:
    n = int(input())

    if n != num:
        intentos -= 1
        if intentos == 0:
            break

        if num > n:
            print("mi número es menor")
        else:
            print("mi número es mayor")
    else:
        correcto = True

if correcto:
    print("Adivinaste, mi número era", num)
else:
    print("No adivinaste, mi numero era", num)