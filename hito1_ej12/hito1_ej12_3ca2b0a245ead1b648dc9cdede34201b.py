#Juego adivina mi número
#Entradas
import random
from random import randint
nGanador= random.randint(1,10)
print("Bienvenido al juego Adivina mi número")
print("Tendrás 5 intentos para lograr adivinar un número del 1 al 20")
i=0

while i<5:
    intento =int(input("Introduzca un número: "))

    if intento > nGanador:
        print("Mi número es menor")
        i=i+1

    elif intento < nGanador:
        print("Mi número es mayor")
        i=i+1

    else:
        print("Adivinaste, mi número era", nGanador)
        i=i+5
        
if i == 5:
    print("No adivinaste, mi número era", nGanador)
      