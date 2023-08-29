#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("Bienvenido al juego Adivina mi número!")
print("He generado un número entre 1 y 20. Tienes 5 intentos para adivinarlo.")

while intentos > 0:
    print("Intentos restantes:", intentos)
    numero_ingresado = int(input("Ingresa tu número: "))

    if numero_ingresado == numero_secreto:
        print("¡Adivinaste! Mi número era", numero_secreto)
        break
    elif numero_ingresado < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")

    intentos -= 1

if intentos == 0:
    print("¡No adivinaste! Mi número era", numero_secreto)   