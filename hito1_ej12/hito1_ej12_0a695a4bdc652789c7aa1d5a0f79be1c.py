import random

# Generar el número secreto aleatoriamente entre 1 y 20
numero_secreto = random.randint(1, 20)

print("¡Bienvenido al juego Adivina mi número!")
print("Tienes 5 intentos para adivinar el número secreto.")

intentos = 0
adivinado = False

while intentos < 5:
    intentos += 1
    numero_ingresado = int(input("Intento #" + str(intentos) + ": Ingresa un número entre 1 y 20: "))

    if numero_ingresado < numero_secreto:
        print("Mi número es mayor.")
    elif numero_ingresado > numero_secreto:
        print("Mi número es menor.")
    else:
        adivinado = True
        break

if adivinado:
    print("¡Adivinaste! Mi número era", numero_secreto)
    sys.exit()
else:
    print("No adivinaste. Mi número era", numero_secreto)


