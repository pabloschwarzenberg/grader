#Juego adivina mi número
import random
from random import randint
def juego(x):
    a=0
    while a<4:
        numeros=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        for i in range(1):
            rand=(random.choice(numeros))
            if x==rand:
                print("Adivinaste, mi número era", x)
            elif x>rand:
                a=a+1
                print("Mi numero es menor")
            elif x<rand:
                a=a+1
                print("Mi numero es mayor")
        x=int(input("Ingresa un numero"))   
    else:
        return str("No adivinaste, mi numero era ") + str(rand)
        
try:
    x=int(input("Ingresa un numero"))
    print(juego(x))
except:
    print("Ingrese un valor valido")