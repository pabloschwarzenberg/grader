#Juego adivina mi número
import random

# Generar un número aleatorio entre 1 y 20
numero_secreto = random.randint(1, 20)

# Número de intentos permitidos
intentos_permitidos = 5

# Ciclo principal del juego
for intento in range(1, intentos_permitidos + 1):
    # Solicitar al jugador que ingrese un número
    numero = int(input("Intento #" + str(intento) + ": Ingresa un número entre 1 y 20: "))

    # Verificar si el número ingresado es igual al número secreto
    if numero == numero_secreto:
        print("Adivinaste, mi número era", numero_secreto)
        break

    # Verificar si el número ingresado es mayor o menor que el número secreto
    if numero < numero_secreto:
        print("Mi número es mayor")
    else:
        print("Mi número es menor")

    # Verificar si se agotaron los intentos
    if intento == intentos_permitidos:
        print("No adivinaste, mi número era", numero_secreto)
      