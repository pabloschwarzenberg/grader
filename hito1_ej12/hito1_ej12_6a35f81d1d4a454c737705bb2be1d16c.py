#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
intentos = 5

for i in range(intentos):
    numero_usuario = int(input("Adivina el número (entre 1 y 20): "))
    if numero_usuario < numero_secreto:
        print("Mi número es mayor")
    elif numero_usuario > numero_secreto:
        print("Mi número es menor")
    else:
        print("Adivinaste, mi número era ", numero_secreto)
        break
else:
    print("No adivinaste, mi número era ", numero_secreto)