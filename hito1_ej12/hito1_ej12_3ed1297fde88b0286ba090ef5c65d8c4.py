import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("¡Bienvenido al juego Adivina mi número!")
print("Estoy pensando en un número del 1 al 20.")

for i in range(intentos):
    print("Intento:", i + 1)
    try:
        numero_adivinar = int(input("Adivina el número: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    if numero_adivinar == numero_secreto:
        print("¡Adivinaste, mi número era", numero_secreto, "!")
        break
    elif numero_adivinar < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")

if numero_adivinar != numero_secreto:
    print("No adivinaste, mi número era", numero_secreto, ". ¡Mejor suerte la próxima vez!")
