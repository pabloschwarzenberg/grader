#Juego adivina mi número
import random

a = random.randint(1, 20)
b = 5

while b > 0:
    numero = int(input())
    if numero == a:
        print("Adivinaste, mi número era", a)
    elif numero > a:
        print("mi número es menor")
    elif numero < a:
        print("mi número es mayor")
    b -= 1
print("No adivinaste, mi número era", a)