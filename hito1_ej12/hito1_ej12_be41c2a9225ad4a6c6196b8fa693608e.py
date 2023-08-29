import random

# Generar un número aleatorio entre 1 y 20
numero_secreto = random.randint(1, 20)

intentos = 5

print("¡Bienvenido al juego Adivina mi número!")
print("Tienes 5 intentos para adivinar el número secreto.")

while intentos > 0:
    # Pedir al jugador que ingrese un número
    numero = int(input("Ingresa un número entre 1 y 20: "))

    # Verificar si el número es menor, mayor o igual al número secreto
    if numero < numero_secreto:
        print("Mi número es mayor.")
    elif numero > numero_secreto:
        print("Mi número es menor.")
    else:
        print("¡Adivinaste, mi número era " + str(numero_secreto) + "!")
        exit()

    intentos -= 1
    print("Te quedan " + str(intentos) + " intentos.")

print("No adivinaste, mi número era " + str(numero_secreto) + ". ¡Mejor suerte la próxima vez!")
