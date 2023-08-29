import random

# Generar número aleatorio entre 1 y 20
numero_secreto = random.randint(1, 20)

print("Bienvenido al juego 'Adivina mi número'!")
print("Tienes 5 intentos para adivinar el número secreto.")

intentos = 0
adivinado = False

while intentos < 5:
    intentos += 1
    numero = int(input("Intento #" + str(intentos) + ": Ingresa un número del 1 al 20: "))

    if numero == numero_secreto:
        adivinado = True
        break
    elif numero < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")

if adivinado:
    print("¡Adivinaste! Mi número era", numero_secreto)
else:
    print("No adivinaste. Mi número era", numero_secreto)
 