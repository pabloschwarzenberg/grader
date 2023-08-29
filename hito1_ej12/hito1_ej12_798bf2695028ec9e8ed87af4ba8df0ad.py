#Juego adivina mi número
import random

# Generar el número aleatorio
numero_secreto = random.randint(1, 20)

# Inicializar el número de intentos y la bandera de adivinanza
intentos = 5
adivinado = False

# Ciclo principal del juego
while intentos > 0:
    # Pedir al jugador que ingrese un número
    numero = int(input("Adivina el número (entre 1 y 20): "))

    # Verificar si el número es menor, mayor o igual al número secreto
    if numero < numero_secreto:
        print("Mi número es mayor.")
    elif numero > numero_secreto:
        print("Mi número es menor.")
    else:
        # El jugador adivinó el número
        adivinado = True
        break

    # Restar un intento
    intentos -= 1

# Mostrar el resultado al jugador
if adivinado:
    print("¡Adivinaste! Mi número era", numero_secreto)
else:
    print("No adivinaste. Mi número era", numero_secreto)
