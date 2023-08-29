#Juego adivina mi número
import random as rnd
a = rnd.randrange(20)
b = 1
n = int(input("Ingrese un número:"))
while b <= 5:
    if n > a:
        print("mi numero es menor, NO ADIVINASTE")
    elif a > n:
        print("mi numero es mayor, NO ADIVINASTE")
    elif a == n:
        print("ADIVINASTE")
    b += 1