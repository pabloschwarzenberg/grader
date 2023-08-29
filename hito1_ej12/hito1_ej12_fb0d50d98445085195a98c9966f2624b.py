#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("Bienvenido al juego Adivina mi número!")
    print("Tienes 5 intentos para adivinar el número secreto, que está entre 1 y 20.")

    while intentos > 0:
        try:
            numero_ingresado = int(input("Ingresa un número: "))
            
            if numero_ingresado == numero_secreto:
                print("¡Adivinaste! Mi número era", numero_secreto)
                return
            elif numero_ingresado < numero_secreto:
                print("Mi número es mayor.")
            else:
                print("Mi número es menor.")
            
            intentos -= 1
            print("Te quedan", intentos, "intentos.\n")
        
        except ValueError:
            print("Ingrese un número válido.\n")
    
    print("¡No adivinaste! Mi número era", numero_secreto)

adivina_mi_numero()

    