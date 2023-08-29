#Juego adivina mi número
# Importar el módulo random para generar números aleatorios
import random

# Generar un número secreto entre 1 y 20
numero_secreto = random.randint(1, 20)

# Inicializar el número de intentos
intentos = 0

# Imprimir las instrucciones del juego
print("Bienvenido al juego adivina mi número.")
print("Tienes 5 intentos para adivinar un número entre 1 y 20.")

# Repetir el juego hasta que se adivine el número o se acaben los intentos
while intentos < 5:
    # Pedir al jugador que ingrese un número
    numero = int(input("Ingresa un número: "))

    # Incrementar el número de intentos
    intentos = intentos + 1

    # Comparar el número ingresado con el número secreto
    if numero == numero_secreto:
        # Si son iguales, el jugador ganó y se termina el juego
        print("Adivinaste, mi número era", numero_secreto)
        break
    elif numero < numero_secreto:
        # Si el número ingresado es menor, se indica al jugador que pruebe con un número mayor
        print("Mi número es mayor.")
    else:
        # Si el número ingresado es mayor, se indica al jugador que pruebe con un número menor
        print("Mi número es menor.")

# Si se acabaron los intentos y el jugador no adivinó, se revela el número secreto y se termina el juego
if intentos == 5 and numero != numero_secreto:
    print("No adivinaste, mi número era", numero_secreto)