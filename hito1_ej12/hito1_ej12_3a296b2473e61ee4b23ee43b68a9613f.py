import random
from random import randint
numero= random.randint(1,10)
print("Bienvenido al juego Adivina mi número")
print("Tendrás 5 intentos para lograr adivinar un número del 1 al 20")
i=0
while i<5:
    intento =int(input("Introduzca un número: "))
    if intento > numero:
        print("Mi número es menor")
        i=i+1
    elif intento < numero:
        print("Mi número es mayor")
        i=i+1

    else:
        print("Adivinaste, mi número era", numero)
        i=i+5
        
if i == 5:
    print("No adivinaste, mi número era", numero)