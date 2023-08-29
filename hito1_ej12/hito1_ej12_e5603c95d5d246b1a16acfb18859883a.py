import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5
    
    print("Bienvenido al juego Adivina mi número!")
    print("He generado un número entre 1 y 20. Tienes 5 intentos para adivinarlo.")
    
    while intentos > 0:
        print("\nIntentos restantes:", intentos)
        numero_ingresado = int(input("Ingresa tu número: "))
        
        if numero_ingresado == numero_secreto:
            print("Adivinaste, mi número era", numero_secreto)
            return
        
        if numero_ingresado < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")
        
        intentos -= 1
    
    print("\nNo adivinaste, mi número era", numero_secreto)

adivina_mi_numero()


     