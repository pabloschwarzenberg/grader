#Juego adivina mi número
import random

import random

def juego():
    intentos=5
    numero=random.randint(1,20)
    while intentos>0:
            print()
            estimacion=int(input("Intenta adivinar el numero: "))
            intentos=intentos-1
            
            if estimacion<numero:
                print("El numero a adivinar es mas grande")
                print("Intentos faltantes: ",intentos)
            if estimacion>numero:
                print("El numero a adivinar es mas pequeño")
                print("Intentos faltantes: ",intentos)
            if estimacion==numero:
                break
    if estimacion==numero:
            numero=str(numero)
            print()
            print("Adivinaste, mi número era "+numero)
    elif estimacion != numero:
            numero=str(numero)
            print()
            print("No adivinaste, mi número era "+numero)
            
if __name__ == "__main__":
    print("hola, estoy pensando en un numero entre 1 y 20")
    juego()