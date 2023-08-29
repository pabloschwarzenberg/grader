#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("¡Bienvenido al juego Adivina mi número!")
print("Estoy pensando en un número del 1 al 20.")
print("Tienes 5 intentos para adivinarlo.")

for i in range(intentos):
    print("Intento", i+1)
    numero_adivinar = int(input("Ingresa tu número: "))

    if numero_adivinar < numero_secreto:
        print("Mi número es mayor.")
    elif numero_adivinar > numero_secreto:
        print("Mi número es menor.")
    else:
        print("Adivinaste, mi número era", numero_secreto)
        break

if numero_adivinar != numero_secreto:
    print("No adivinaste, mi número era", numero_secreto)