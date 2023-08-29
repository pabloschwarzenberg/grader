#Juego adivina mi número
import random

# Generar el número secreto
numero_secreto = random.randint(1, 20)

# Inicializar el contador de intentos
intentos = 0

# Bucle principal del juego
while intentos < 5:
    # Pedir al usuario que adivine el número
    adivinanza = int(input("Adivina mi número: "))

    # Incrementar el contador de intentos
    intentos += 1

    # Verificar si la adivinanza es correcta
    if adivinanza == numero_secreto:
        print("Adivinaste, mi número era", numero_secreto)
        break
    elif adivinanza < numero_secreto:
        print("Mi número es mayor")
    else:
        print("Mi número es menor")

# Verificar si el usuario no adivinó el número
if intentos == 5:
    print("No adivinaste, mi número era", numero_secreto)
