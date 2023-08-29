import random

# Generar número secreto aleatorio entre 1 y 20
numero_secreto = random.randint(1, 20)

print("¡Bienvenido al juego Adivina mi número!")
print("Tienes 5 intentos para adivinar el número secreto.")

intentos = 0
adivinado = False

while intentos < 5:
    intentos += 1
    numero_ingresado = int(input("Intento #" + str(intentos) + ": Ingresa un número entre 1 y 20: "))

    if numero_ingresado == numero_secreto:
        adivinado = True
        break
    elif numero_ingresado < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")

if adivinado:
    print("¡Adivinaste, mi número era", numero_secreto)
else:
    print("No adivinaste, mi número era", numero_secreto)
