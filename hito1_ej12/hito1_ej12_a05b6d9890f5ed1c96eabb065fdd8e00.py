import random

numero_secreto = random.randint(1, 20)
intentos = 5

print("Bienvenido al juego Adivina mi número!")
print("Tienes 5 intentos para adivinar un número entre 1 y 20.")

for i in range(intentos):
    intento = int(input("Intento {}/{}: Ingresa tu número: ".format(i + 1, intentos)))

    if intento == numero_secreto:
        print("Adivinaste, ¡mi número era {}!".format(numero_secreto))
        break

    if intento < numero_secreto:
        print("Mi número es mayor.")
    else:
        print("Mi número es menor.")
else:
    print("No adivinaste, mi número era {}.".format(numero_secreto))

print("Gracias por jugar. ¡Hasta la próxima!")
