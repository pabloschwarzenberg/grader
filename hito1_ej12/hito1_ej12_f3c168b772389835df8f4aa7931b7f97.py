#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("Tienes 5 intentos para adivinar el número secreto.")

    while intentos > 0:
        try:
            adivinanza = int(input("Ingresa tu número (entre 1 y 20): "))
            if adivinanza < 1 or adivinanza > 20:
                print("El número debe estar entre 1 y 20. Intenta nuevamente.")
                continue
        except ValueError:
            print("Entrada inválida. Debes ingresar un número. Intenta nuevamente.")
            continue

        if adivinanza == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        if adivinanza < numero_secreto:
            print("Mi número es mayor. Inténtalo nuevamente.")
        else:
            print("Mi número es menor. Inténtalo nuevamente.")

        intentos -= 1
        print("Te quedan", intentos, "intentos.")

    print("No adivinaste. Mi número era", numero_secreto)

adivina_mi_numero()
      