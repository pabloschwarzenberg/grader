import random

intentos= 0
numero = random.randint(1, 20)
while intentos< 5:
    estimacion= int(input("Ingrese un numero del 1 al 20"))
    intentos=intentos+ 1
    if estimacion < numero:
        print("mi número es mayor")
    elif estimacion > numero:
        print("mi número es menor")
    elif estimacion == numero:
        break
if estimacion == numero:
    intentos= str(intentos)
    print("Adivinaste, mi número era",numero)
elif estimacion != numero:
    numero = str(numero)
    print("No adivinaste, mi número era",numero)     