import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5
    
    while intentos > 0:
        intento = int(input("Intenta adivinar mi número (entre 1 y 20): "))
        
        if intento == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return
        elif intento < numero_secreto:
            print("Mi número es mayor")
        else:
            print("Mi número es menor")
        
        intentos -= 1
    
    print("No adivinaste. Mi número era", numero_secreto)

adivina_mi_numero()