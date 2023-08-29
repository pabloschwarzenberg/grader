#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5
    
    print("¡Bienvenido a Adivina mi número!")
    print("He generado un número entre 1 y 20. Tienes 5 intentos para adivinarlo.")
    
    while intentos > 0:
        print("Intentos restantes:", intentos)
        guess = int(input("Ingresa tu número: "))
        
        if guess == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return
        
        if guess < numero_secreto:
            print("Mi número es mayor")
        else:
            print("Mi número es menor")
        
        intentos -= 1
    
    print("¡No adivinaste! Mi número era", numero_secreto)

adivina_mi_numero()
 