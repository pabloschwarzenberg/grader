import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("¡Bienvenido al juego Adivina mi número!")
print("Tienes 5 intentos para adivinar el número secreto.")

for i in range(intentos):
    print("Intento #" + str(i + 1))
    numero_ingresado = int(input("Ingresa un número entre 1 y 20: "))

    if numero_ingresado == numero_secreto:
        print("¡Adivinaste, mi número era " + str(numero_secreto) + "!")
        break
    elif numero_ingresado < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")

    if i == intentos - 1:
        print("No adivinaste, mi número era " + str(numero_secreto) + ".")
        break

print("Gracias por jugar Adivina mi número. ¡Hasta la próxima!")
