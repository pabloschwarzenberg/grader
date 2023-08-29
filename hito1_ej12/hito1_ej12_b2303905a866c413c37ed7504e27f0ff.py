import random

def generar_numero_secreto():
    return random.randint(1, 20)

numero_secreto = generar_numero_secreto()
intentos = 5

print("¡Bienvenido al juego 'Adivina mi número'!")
print("Estoy pensando en un número entre 1 y 20. Tienes 5 intentos para adivinarlo.")

while intentos > 0:
    print("Intentos restantes:", intentos)
    numero = int(input("Ingresa un número: "))

    if numero == numero_secreto:
        print("¡Adivinaste, mi número era", numero_secreto)
        break

    if numero < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")

    intentos -= 1

if intentos == 0:
    print("No adivinaste, mi número era", numero_secreto)
      