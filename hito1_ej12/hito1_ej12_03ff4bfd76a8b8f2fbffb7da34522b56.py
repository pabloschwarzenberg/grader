#Juego adivina mi número
import random
numero_secreto = random.randint(1, 20)
intentos = 5
print("¡Bienvenido al juego Adivina mi Número!")
print("Tienes", intentos, "intentos para adivinar mi número secreto entre 1 y 20.")
for i in range(intentos):
    intento = int(input("Introduce un número: "))
    if intento < numero_secreto:
        print("Mi número es mayor.")
    elif intento > numero_secreto:
        print("Mi número es menor.")
    else:
        print("¡Adivinaste, mi número era", numero_secreto, "!")
        break
if intento != numero_secreto:
    print("No adivinaste, mi número era", numero_secreto)
      