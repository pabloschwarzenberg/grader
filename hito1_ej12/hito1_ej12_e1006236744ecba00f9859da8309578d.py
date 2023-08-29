#Juego adivina mi número
import random
from random import randint
N1 = 1
N2 = 20
N = random.randint(N1,N2)
intentos = 1
while intentos <=5:
    NJ = int(input("adivine el numero:"))
    
    if N > NJ :
        print("mi numero es mayor")
    else:
        print("mi numero es menor")
        
    if N == NJ:
        print("Adivinaste, mi número era:",N,"")
        break
        
    if intentos == 5:
        print("No adivinaste, mi número era:",N,"")
        
    intentos += 1