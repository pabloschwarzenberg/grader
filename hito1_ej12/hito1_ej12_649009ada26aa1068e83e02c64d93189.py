import random

numero_secreto = random.randint(1, 20)
intentos = 0
max_intentos = 5

print("Bienvenido al juego Adivina mi número.")
print("Tienes que adivinar un número del 1 al 20.")
print("Tienes 5 intentos.")

while intentos < max_intentos:
    intentos += 1
    numero_ingresado = int(input("Intento {}: Ingresa un número: ".format(intentos)))

    if numero_ingresado == numero_secreto:
        print("¡Adivinaste! Mi número era", numero_secreto)
        break
    elif numero_ingresado < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")

    if intentos == max_intentos:
        print("No adivinaste. Mi número era", numero_secreto)
        break

if intentos == max_intentos and numero_ingresado != numero_secreto:
    print("No adivinaste. Mi número era", numero_secreto)

print("Gracias por jugar.")
