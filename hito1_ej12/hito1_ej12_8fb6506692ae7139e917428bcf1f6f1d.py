import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("Tienes 5 intentos para adivinar el número secreto.")

    while intentos > 0:
        print("Intento restante:", intentos)
        adivinanza = int(input("Ingresa tu número: "))

        if adivinanza == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        if adivinanza < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

        intentos -= 1

    print("No adivinaste. Mi número era", numero_secreto)

#Ejecutar el juego
adivina_mi_numero()