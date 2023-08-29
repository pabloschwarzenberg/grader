import random

numero_secreto = random.randint(1, 20)
intentos = 5

for i in range(intentos):
    intento = int(input("Adivina el número (entre 1 y 20): "))

    if intento < numero_secreto:
        print("Mi número es mayor.")
    elif intento > numero_secreto:
        print("Mi número es menor.")
    else:
        print("¡Adivinaste, mi número era", numero_secreto,)
        break

if intento != numero_secreto:
    print("No adivinaste, mi número era", numero_secreto, )