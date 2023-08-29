#Juego adivina mi número
import random

# Generar número secreto aleatorio entre 1 y 20
numero_secreto = random.randint(1, 20)

# Inicializar contador de intentos
intentos = 0

print("Bienvenido al juego Adivina mi número!")
print("Tienes 5 intentos para adivinar el número secreto.")

while intentos < 5:
    # Solicitar al jugador que ingrese un número
    numero = int(input("Ingresa un número entre 1 y 20: "))

    # Verificar si el número ingresado es menor, mayor o igual al número secreto
    if numero < numero_secreto:
        print("Mi número es mayor.")
    elif numero > numero_secreto:
        print("Mi número es menor.")
    else:
        print("¡Adivinaste, mi número era", numero_secreto, "!")
        break

    # Incrementar el contador de intentos
    intentos += 1

if intentos == 5:
    print("No adivinaste, mi número era", numero_secreto)