import random

numero_secreto = random.randint(1, 20)  # Generar número aleatorio entre 1 y 20
intentos = 5  # Número de intentos permitidos

print("¡Bienvenido al juego 'Adivina mi número'!")
print("Tienes que adivinar un número entre 1 y 20. ¡Buena suerte!")

while intentos > 0:
    # Ingreso del número por parte del jugador
    numero_adivinar = int(input("Ingresa tu número: "))

    # Comparación del número ingresado con el número secreto
    if numero_adivinar == numero_secreto:
        print("¡Adivinaste! Mi número era", numero_secreto)
        break
    elif numero_adivinar < numero_secreto:
        print("Mi número es mayor")
    else:
        print("Mi número es menor")

    intentos -= 1
    print("Te quedan", intentos, "intentos")

# Si se acabaron los intentos sin adivinar el número
if intentos == 0:
    print("No adivinaste. Mi número era", numero_secreto)
      