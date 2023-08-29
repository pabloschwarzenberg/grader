import random

# Generar el número secreto aleatoriamente
numero_secreto = random.randint(1, 20)

print("¡Bienvenido al juego 'Adivina mi número'!")
print("Tienes 5 intentos para adivinar el número secreto (entre 1 y 20).")

intentos = 0
adivinado = False

while intentos < 5:
    intentos += 1
    numero_ingresado = int(input("Intento {}: Ingresa un número: ".format(intentos)))

    if numero_ingresado == numero_secreto:
        adivinado = True
        break
    elif numero_ingresado < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")

if adivinado:
    print("¡Adivinaste! Mi número era", numero_secreto)
else:
    print("No adivinaste. Mi número era", numero_secreto)