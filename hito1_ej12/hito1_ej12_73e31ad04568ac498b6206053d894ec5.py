#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)

print("Bienvenido al juego 'Adivina mi número'")

intentos = 5
adivinado = False

for i in range(intentos):
    numero_ingresado = int(input("Intento {} de {}: Ingresa un número entre 1 y 20: ".format(i+1, intentos)))

    if numero_ingresado < numero_secreto:
        print("Mi número es mayor")
    elif numero_ingresado > numero_secreto:
        print("Mi número es menor")
    else:
        adivinado = True
        break

if adivinado:
    print("¡Adivinaste! Mi número era", numero_secreto)
else:
    print("No adivinaste. Mi número era", numero_secreto)     