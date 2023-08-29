import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("He generado un número entre 1 y 20. Tienes 5 intentos para adivinarlo.")

    for i in range(intentos):
        print(f"Intento {i+1}")
        numero_ingresado = int(input("Ingresa tu número: "))

        if numero_ingresado == numero_secreto:
            print("¡Adivinaste! ¡Mi número era", numero_secreto, "!")
            return

        if numero_ingresado < numero_secreto:
            print("Mi número es mayor.")

        if numero_ingresado > numero_secreto:
            print("Mi número es menor.")

    print("No adivinaste. ¡Mi número era", numero_secreto, "!")

if __name__ == "__main__":
    adivina_mi_numero()
