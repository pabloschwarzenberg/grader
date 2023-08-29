#Juego adivina mi número
import random

secreto = random.randint(1, 20)
intentos = 5

print("Bienvenido al juego Adivina mi número!")
print("Tienes 5 intentos para adivinar el número secreto, que está entre 1 y 20.")

for i in range(intentos):
    print("Intento", i+1)
    numero = int(input("Ingresa tu número: "))

    if numero == secreto:
        print("Adivinaste, mi número era", secreto)
        break
    elif numero < secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")

if numero != secreto:
    print("No adivinaste, mi número era", secreto)
