import random

numero_secreto = random.randint(1,20)

intentos = 5

for i in range(intentos):
    print("Intento", i + 1)
    entrada = int(input("Ingresa un número entre 1 y 20: "))
    if entrada == numero_secreto:
        print("Adivinaste, mi número era", numero_secreto)
        break
    elif entrada < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")
else:
    print("No adivinaste, mi número era", numero_secreto)
     