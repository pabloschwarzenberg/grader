#Juego adivina mi número
import time

tiempo = time.time()
numero_secreto = int((tiempo - int(tiempo)) * 20) + 1
intentos = 5

print("¡Bienvenido al juego Adivina mi número!")
print("Tienes 5 intentos para adivinar el número secreto entre 1 y 20.")

for i in range(intentos):
    print("Intento", i + 1)
    numero_ingresado = int(input("Ingresa un número: "))

    if numero_ingresado < numero_secreto:
        print("Mi número es mayor.")
    elif numero_ingresado > numero_secreto:
        print("Mi número es menor.")
    else:
        print("¡Adivinaste! Mi número era", numero_secreto)
        break

if numero_ingresado != numero_secreto:
    print("No adivinaste. Mi número era", numero_secreto)      