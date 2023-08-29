#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("¡Bienvenido al juego Adivina mi número!")
print("Tienes 5 intentos para adivinar el número secreto.")

for i in range(intentos):
    numero_ingresado = int(input("Intento #" + str(i + 1) + ": Ingresa un número del 1 al 20: "))
    
    if numero_ingresado == numero_secreto:
        print("¡Adivinaste! Mi número era", numero_secreto)
        break
    elif numero_ingresado < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")

if numero_ingresado != numero_secreto:
    print("No adivinaste. Mi número era", numero_secreto)