#Juego adivina mi número
import random
N = int(random.randrange(21))
I = 5
N2 = 0
while I != 0 :
    N2 = int(input("Ingrese numero: "))
    if N2 < N:
        print("Mi número es mayor")
        I = I - 1
    elif N2 > N :
        print("Mi número es menor")
        I = I - 1
    else:
        I = 0
if N2 == N:
    print("Adivinaste, mi número era ",N)
else:
    print("No adivinaste, mi número era ",N)