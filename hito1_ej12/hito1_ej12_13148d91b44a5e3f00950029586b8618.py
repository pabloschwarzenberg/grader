#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 0
    
    print("Bienvenido a 'Adivina mi número'!")
    print("Tienes 5 intentos para adivinar el número secreto.")
    
    while intentos < 5:
        intentos += 1
        numero_ingresado = int(input("Intento {}: Ingresa un número entre 1 y 20: ".format(intentos)))
        
        if numero_ingresado < numero_secreto:
            print("Mi número es mayor")
        elif numero_ingresado > numero_secreto:
            print("Mi número es menor")
        else:
            print("Adivinaste, mi número era", numero_secreto)
            return
    
    print("No adivinaste, mi número era", numero_secreto)

# Ejecutar el juego
adivina_mi_numero()
      