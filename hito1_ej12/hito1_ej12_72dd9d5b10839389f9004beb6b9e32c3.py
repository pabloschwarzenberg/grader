#Juego adivina mi número
 import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("adivina el numero")

for i in range(intentos):
    numero_ingresado = int(input("Ingresa un número entre 1 y 20: "))

    if numero_ingresado == numero_secreto:
        print("¡Adivinaste!")
        break
    elif numero_ingresado < numero_secreto:
        print("Mi número es mayor")
    else:
        print("Mi número es menor")

if numero_ingresado != numero_secreto:
    print("No adivinaste, mi número era", numero_secreto)

print("listo")     