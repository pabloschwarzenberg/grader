#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5
    
    print("¡Bienvenido al juego Adivina mi número!")
    print("Tienes 5 intentos para adivinar el número secreto, ¡buena suerte!\n")
    
    while intentos > 0:
        intento = int(input("Ingresa un número entre 1 y 20: "))
        
        if intento < numero_secreto:
            print("Mi número es mayor. Intenta nuevamente.\n")
        elif intento > numero_secreto:
            print("Mi número es menor. Intenta nuevamente.\n")
        else:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return
        
        intentos -= 1
    
    print("No adivinaste. Mi número era", numero_secreto)

# Llamada a la función principal
adivina_mi_numero()
      