#Juego adivina mi número
import random
import sys
N = random.randrange(1,20)
print("Juguemos a adivinar el número, yo elegiré un numero aleatoriamente con un rango del 1 al 20, tu debes ingresar un número y trata de adivinarlo,"
      "Tienes solamente 5 intentos, ¡TE DESEO SUERTE")
X = eval(input("Ingresa un número: "))
if X == N:
    print("Adivinaste, mi número era",N)
    sys.exit()
else:
    if X<N:
        print("Mi número es mayor")
    else:
        if X>N:
            print("Mi número es menor")

    A=int(input("Ingresa un número: "))
    if A == N:
        print("Adivinaste, mi número era: ",N)
        sys.exit()
    else:
        if A < N:
            print("Mi número es mayor")
        else:
            if A > N:
                print("Mi número es menor")

    Y = int(input("Ingresa un número: "))
    if Y == N:
        print("Adivinaste, mi número era", N)
        sys.exit()
    else:
        if Y < N:
            print("Mi número es mayor")
        else:
            if Y > N:
                print("Mi número es menor")
    Z = int(input("Ingresa un número: "))
    if Z == N:
        print("Adivinaste, mi número era", N)
        
    else:
        if Z < N:
            print("Mi número es mayor")
        else:
            if Z > N:
                print("Mi número es menor")
    B = int(input("Ingresa un número: "))
    if B == N:
        print("Adivinaste, mi número era: ", N)
        sys.exit()
    elif B!= N:
        print("No adivinaste, mi número era: ",N)
