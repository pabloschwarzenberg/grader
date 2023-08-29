import random

numero_secreto = random.randint(1, 20)
intentos_restantes = 5

print("¡Bienvenido al juego de adivinanza de números!")
print("Estoy pensando en un número entre 1 y 20.")
print("Tienes 5 intentos para adivinar mi número.")

while intentos_restantes > 0:
    print("Te quedan", intentos_restantes, "intentos.")
    intento = int(input("¿Cuál es tu intento? "))

    if intento < numero_secreto:
        print("Mi número es mayor.")
    elif intento > numero_secreto:
        print("Mi número es menor.")
    else:
        break

    intentos_restantes -= 1

if intento == numero_secreto:
    print("¡Adivinaste! Mi número era", numero_secreto)
else:
    print("No adivinaste. Mi número era", numero_secreto)