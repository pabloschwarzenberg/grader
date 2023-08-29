#Juego adivina mi número
import random

rnd = random.randint(1, 20)
n = 0
ronda = 0
while n != rnd and ronda != 5:
    n = int(input("Ingresa un número: "))
    if n > rnd:
        print("mi número es menor")
    elif n < rnd:
        print("mi número es mayor")

    ronda += 1

if n == rnd:
    print("Adivinaste, mi número era", n)

else:
    print("No adivinaste, mi número era", rnd)