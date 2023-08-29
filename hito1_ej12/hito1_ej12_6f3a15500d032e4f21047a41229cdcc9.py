#Juego adivina mi número
import random

# Generar un número aleatorio entre 1 y 20
numero_secreto = random.randint(1, 20)

print("Bienvenido al juego Adivina mi número!")
print("Tienes 5 intentos para adivinar el número secreto.")

intentos = 0

while intentos < 5:
    # Pedir al jugador que ingrese un número
    numero_ingresado = int(input("Ingresa un número entre 1 y 20: "))

    if numero_ingresado < numero_secreto:
        print("Mi número es mayor.")
    elif numero_ingresado > numero_secreto:
        print("Mi número es menor.")
    else:
        print("¡Adivinaste! Mi número era", numero_secreto)
        break

    intentos += 1

if intentos == 5:
    print("No adivinaste. Mi número era", numero_secreto)
      