#Juego adivina mi número
import random
def adivina_numero():
    numero_secreto=random.randint(1,20)
    intentos=5

    print("Bienvenido al juego Adivina mi numero")
    print("Tienes 5 intentos para adivinar el numero secreto, del 1 al 20")

    while intentos>0:
        print("Te quedan: ",intentos," restantes")
        numero=int(input("Ingresa tu numero: "))

        if numero==numero_secreto:
            print("Adivinaste,mi numero era:",numero_secreto)
            return
        if numero<numero_secreto:
            print("Mi numero es mayor")
        else:
            print("Mi numero es menor")
        intentos=intentos-1
    print("No adivinaste, mi numero era:",numero_secreto)
adivina_numero()      