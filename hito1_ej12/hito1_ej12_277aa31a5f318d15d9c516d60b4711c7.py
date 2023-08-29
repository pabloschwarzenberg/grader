#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("Tienes 5 intentos para adivinar el numero secreto entre 1 y 20.")

for i in range(intentos):
    print("\nIntento", i + 1)
    numero = int(input("Ingresa un número: "))

    if numero == numero_secreto:
        print("Adivinaste! Mi numero era", numero_secreto)
        break
    elif numero < numero_secreto:
        print("Mi numero es mayor")
    else:
        print("Mi numero es menor")

if numero != numero_secreto:
    print("\nNo adivinaste. Mi número era", numero_secreto)
      