#Juego adivina mi número
import random
x = random.randint(1, 20)
intentos = 0

print(x)
while intentos < 5:
    print("ingrese numero")
    numero = input()
    numero = int(numero)

    intentos = intentos + 1

    if numero > x:
        print("mi numero es menor")

    if numero < x:
        print("mi numero es mayor")

    if numero == x:
        break

if numero == x:
    print("adivinaste el numero era", x)

if numero != x:
    print("no adivinaste el numero era", x)
