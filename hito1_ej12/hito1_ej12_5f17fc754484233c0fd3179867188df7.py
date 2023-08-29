import random

def adivina_mi_numero():
    # Generar número secreto aleatorio entre 1 y 20
    numero_secreto = random.randint(1, 20)
    
    # Inicializar contador de intentos
    intentos = 0
    
    # Ciclo principal del juego
    while intentos < 5:
        # Pedir al jugador que ingrese un número
        numero = int(input("Intento {}: Ingresa un número entre 1 y 20: ".format(intentos+1)))
        
        # Verificar si el número es igual al número secreto
        if numero == numero_secreto:
            print("Adivinaste, mi número era", numero_secreto)
            return
        
        # Verificar si el número es menor al número secreto
        elif numero < numero_secreto:
            print("Mi número es mayor")
        
        # El número es mayor al número secreto
        else:
            print("Mi número es menor")
        
        # Incrementar contador de intentos
        intentos += 1
    
    # Si se superan los 5 intentos, mostrar el número secreto
    print("No adivinaste, mi número era", numero_secreto)

# Ejecutar el juego "Adivina mi número"
adivina_mi_numero()      