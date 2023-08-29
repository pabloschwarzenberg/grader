#Juego adivina mi número
import random

numero_secreto = random.randint(1, 20)
intentos_maximos = 5
intentos_realizados = 0

print("¡Bienvenido al juego Adivina mi número!")
print("Tienes que adivinar un número entre 1 y 20. Tienes 5 intentos.")

while intentos_realizados < intentos_maximos:
    numero_ingresado = int(input("Ingresa un número: "))
    intentos_realizados += 1
    
    if numero_ingresado == numero_secreto:
        print("¡Adivinaste! Mi número era", numero_secreto)
        break
    elif numero_ingresado < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")

if intentos_realizados == intentos_maximos:
    print("No adivinaste. Mi número era", numero_secreto)
    