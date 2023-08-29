#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("¡Bienvenido al juego 'Adivina mi número'!")
print("Tienes 5 intentos para adivinar el número secreto.")

for i in range(intentos):
    print("Intento", i+1)
    numero_adivinar = int(input("Ingresa un número del 1 al 20: "))

    if numero_adivinar == numero_secreto:
        print("¡Adivinaste! Mi número era", numero_secreto)
        break
    elif numero_adivinar < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")

if numero_adivinar != numero_secreto:
    print("No adivinaste. Mi número era", numero_secreto)
      