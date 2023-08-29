import random

# Generar el número secreto aleatoriamente
numero_secreto = random.randint(1, 20)

print("¡Bienvenido al juego Adivina mi número!")
print("Tienes 5 intentos para adivinar el número secreto.")

intentos = 0

while intentos < 5:
    intentos += 1
    numero_ingresado = int(input("Intento {}: Ingresa un número entre 1 y 20: ".format(intentos)))

    if numero_ingresado == numero_secreto:
        print("¡Adivinaste! Mi número era", numero_secreto)
        break
    elif numero_ingresado < numero_secreto:
        print("Mi número es mayor")
    else:
        print("Mi número es menor")

if intentos == 5:
    print("No adivinaste. Mi número era", numero_secreto)
      