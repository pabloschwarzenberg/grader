import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5
    
    print("¡Bienvenido al juego Adivina el numero")
    print("Tiene que elegir un numero entre el 1 y el 20. Tienes 5 intentos para adivinarlo.")

    while intentos > 0:
        intento = int(input("Ingresa tu número: "))
        
        if intento == numero_secreto:
            print("Correcto, mi numero era", numero_secreto)
            return
        
        if intento < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")
        
        intentos -= 1
        print("Te quedan", intentos, "intentos.")
    
    print("No lo lograste. Mi número era", numero_secreto)

adivina_mi_numero()
