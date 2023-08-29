#Juego adivina mi número
import random
valor_aleatorio = random.randint(1,20)

while True:
    numero_1 = eval(input("ingrese el primer intento: "))

    if numero_1 > valor_aleatorio:
        print("mi número es mayor")
    
    elif numero_1 < valor_aleatorio:
        print("mi número es menor")

    if numero_1 == valor_aleatorio:
        print("adivinaste, mi numero era: ",valor_aleatorio)
        break

    numero_2 = eval(input("ingrese el segundo intento: "))

    if numero_2 > valor_aleatorio:
        print("mi número es mayor")
    
    elif numero_2 < valor_aleatorio:
        print("mi número es menor")
    
    if numero_2 == valor_aleatorio:
        print("adivinaste, mi numero era: ",valor_aleatorio)
        break
    
    numero_3 = eval(input("ingrese el tercer intento:"))

    if numero_3 > valor_aleatorio:
        print("mi número es mayor")
    
    elif numero_3 < valor_aleatorio:
        print("mi número es menor")

    if numero_3== valor_aleatorio:
        print("adivinaste, mi numero era: ",valor_aleatorio)
        break

    numero_4 = eval(input("ingrese el cuarto intento: "))

    if numero_4 > valor_aleatorio:
        print("mi número es mayor")
    
    elif numero_4 < valor_aleatorio:
        print("mi número es menor")

    if numero_4 == valor_aleatorio:
        print("adivinaste, mi numero era: ",valor_aleatorio)
        break
    
    numero_5 = eval(input("ingrese el quinto intento: "))

    if numero_5 > valor_aleatorio:
        print("mi número es mayor")
    
    elif numero_5 < valor_aleatorio:
        print("mi número es menor")

    if numero_5 == valor_aleatorio:
        print("adivinaste, mi numero era: ",valor_aleatorio)
        break

    else:
       print("No adivinaste, mi número era: ",valor_aleatorio)
       
    break