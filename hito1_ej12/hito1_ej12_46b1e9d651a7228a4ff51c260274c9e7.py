#Juego adivina mi número
 import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("¡Bienvenido a 'Adivina mi número'!")
print("Estoy pensando en un número entre 1 y 20. Tienes 5 intentos para adivinarlo.")

while intentos > 0:
    numero = int(input("Ingresa tu intento: "))

    if numero < numero_secreto:
        print("Mi número es mayor.")
    elif numero > numero_secreto:
        print("Mi número es menor.")
    else:
        print("¡Adivinaste! Mi número era", numero_secreto)
        break

    intentos -= 1
    print("Te quedan", intentos, "intentos.")

if intentos == 0:
    print("No adivinaste. Mi número era", numero_secreto)

print("¡Gracias por jugar!")
     