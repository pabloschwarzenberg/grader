#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("Este es el juego Adivina mi Numero")
print("Tienes 5 intentos para adivinar el número secreto, que está entre 1 y 20.")

while intentos > 0:
    intentos -= 1
    numero_ingresado = int(input("Ingresa un numero: "))

    if numero_ingresado == numero_secreto:
        print("Adivinaste, mi numero era" ,numero_secreto)
        break
    elif numero_ingresado < numero_secreto:
        print("mi numero es mayor.")
    else:
        print("mi numero es menor.")

    if intentos > 0:
        print("Tienes", intentos, "intentos restantes.")

if intentos == 0:
    print("No adivinaste, mi numero era" ,numero_secreto)