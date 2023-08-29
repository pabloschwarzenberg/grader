#Juego adivina mi número
from random import * 

R = randint(1, 20)

for I in range(1, 6):
    U = int(input("Ingrese un numero: "))
    if U > R:
        print("El numero es menor")
    elif U < R:
        print("El numero es mayor")
    elif U == R: 
        print("Correcto, el numero es ", R)
        break

if I == 5:
 print("No adivinaste, mi número era", R)
