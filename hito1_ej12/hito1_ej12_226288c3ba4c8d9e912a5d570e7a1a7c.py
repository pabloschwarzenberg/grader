import random

# Generar número secreto
numero_secreto = random.randint(1, 20)

# Inicializar número de intentos
intentos_restantes = 5

print("¡Bienvenido al juego Adivina mi número!")
print("Tienes 5 intentos para adivinar un número entre 1 y 20.")

while intentos_restantes > 0:
    # Pedir al jugador que ingrese un número
    numero_ingresado = int(input("Ingresa tu intento: "))

    # Verificar si el número ingresado es igual al número secreto
    if numero_ingresado == numero_secreto:
        print("¡Adivinaste, mi número era", numero_secreto, "!")
        break
    elif numero_ingresado < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")

    # Reducir el número de intentos restantes
    intentos_restantes -= 1

    # Imprimir el número de intentos restantes
    print("Intentos restantes:", intentos_restantes)

# Verificar si se agotaron los intentos
if intentos_restantes == 0:
    print("No adivinaste, mi número era", numero_secreto)