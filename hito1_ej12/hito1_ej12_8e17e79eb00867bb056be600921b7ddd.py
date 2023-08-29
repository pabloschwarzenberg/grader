import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("¡Bienvenido al juego 'Adivina mi número'!")
print("Tienes 5 intentos para adivinar el número secreto.")

adivinado = False

while intentos > 0 and not adivinado:
    numero_ingresado = int(input("Ingresa un número del 1 al 20: "))

    if numero_ingresado == numero_secreto:
        print("¡Adivinaste! Mi número era", numero_secreto)
        adivinado = True
    elif numero_ingresado < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")

    intentos -= 1

if not adivinado:
    print("¡No adivinaste! Mi número era", numero_secreto)

print("¡Gracias por jugar!")
