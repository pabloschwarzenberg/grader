#Juego adivina mi número
import random

r = random.randint(1,20)
while True:
    a = 1
    intentos = a + 1
    n = input()
    if n == r:
        print("adivinaste, mi numero era: ", r)
        break
    else:
        if intentos == 6:
            print("No adivinaste, mi número era", r)
            break