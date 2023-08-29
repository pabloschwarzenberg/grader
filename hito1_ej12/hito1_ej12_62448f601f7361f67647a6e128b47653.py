#Juego adivina mi número
import random
x = random.randint(1, 20)
intentos = 4
print("Hola!, adivina el número que estoy pensando")
numero = int(input("Ingresa tu número: "))
if intentos == 0:
    print("No adivinaste, mi número era:", x)
while numero != x:
    if numero > x:
            intentos -= 1
            print("Mi número es menor")
            numero = int(input("Intenta de nuevo: "))
    elif numero < x:
            intentos -= 1
            print("Mi número es mayor")
            numero = int(input("Intenta de nuevo: "))
if numero == x:
    print("Adivinaste, mi número era:", x)
