#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("¡Bienvenido a Adivina Mi Número!")
print("Tienes 5 intentos para adivinar un número entre 1 y 20.")

while intentos > 0:
    numero_ingresado = int(input("Ingresa un número: "))

    if numero_ingresado == numero_secreto:
        print("Adivinaste, ¡mi número era", numero_secreto, "!")
        break
    elif numero_ingresado < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")

    intentos -= 1

if intentos == 0:
    print("No adivinaste, ¡mi número era", numero_secreto, "!")

print("Gracias por jugar. ¡Hasta luego!")
