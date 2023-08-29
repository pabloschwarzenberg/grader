#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("¡Bienvenido a Adivina mi número!")
print("Tienes 5 intentos para adivinar el número secreto.")

for i in range(intentos):
    print(f"Intento {i+1}:")
    numero_ingresado = int(input("Ingresa un número entre 1 y 20: "))

    if numero_ingresado < numero_secreto:
        print("Mi número es mayor.")
    elif numero_ingresado > numero_secreto:
        print("Mi número es menor.")
    else:
        print(f"Adivinaste, mi número era {numero_secreto}.")
        break

if numero_ingresado != numero_secreto:
    print(f"No adivinaste, mi número era {numero_secreto}.")
      