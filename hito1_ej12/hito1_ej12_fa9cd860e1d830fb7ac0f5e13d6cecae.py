import random

def rand():
    return random.randint(1, 20)

def juego():
    x = 5001
    numero = rand()
    intento = 0
    while intento != 5:
        x = int(input("Ingresa un numero: "))
        tuNumero(x, numero)
        intento += 1
        if x == numero:
            break
    if intento == 5:
        print("No adivinaste, mi número era "+str(numero))

def tuNumero(x, numero):
    if x < numero:
        print("mi número es menor")
    if x > numero:
        print("mi número es mayor")
    if x == numero:
        print("Adivinaste, mi número era "+str(numero))
        
        
juego()