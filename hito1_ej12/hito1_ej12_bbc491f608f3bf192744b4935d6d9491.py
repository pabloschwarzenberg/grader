#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("¡Bienvenido al juego Adivina mi número!")
print("Estoy pensando en un número del 1 al 20. Tienes 5 intentos para adivinarlo.")

adivinado = False

while intentos > 0 and not adivinado:
    print("Intentos restantes:", intentos)
    numero = int(input("Ingresa un número: "))

    if numero == numero_secreto:
        print("Adivinaste, mi número era ", numero_secreto)
        adivinado = True
    elif numero < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")

    intentos -= 1

if not adivinado:
    print("No adivinaste, mi número era ", numero_secreto)