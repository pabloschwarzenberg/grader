#Juego adivina mi número
from random import randint

intentos = 1
valorAleatorio = randint(1,20)

while intentos <= 5:
    numeroIngresar = int(input("Adivina mi número: "))

    if numeroIngresar < valorAleatorio:
        print("Mi número es mayor")
    elif numeroIngresar > valorAleatorio:
        print("Mi número es menor")
    elif numeroIngresar == valorAleatorio:
        print("Adivinaste, mi número era ", valorAleatorio)
        break

    intentos += 1

    if intentos == 6:    
        print("No adivinaste, mi número era ", valorAleatorio) 