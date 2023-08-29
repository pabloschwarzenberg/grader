import random
from random import randint
x = 1
y = 20
numero_secreto = random.randint(x, y)
intentos = 5

while intentos > 0:
    n = int(input("Adivine el numero: "))
    if n == numero_secreto:
        print("Adivinaste, mi número era: ", numero_secreto)
        break
    elif n < numero_secreto:
        print("mi numero es mayor")
        intentos = intentos - 1
    else:
         print("mi numero es menor")
         intentos = intentos - 1
if intentos == 0:
    print("No adivinaste mi numero era: ", numero_secreto)