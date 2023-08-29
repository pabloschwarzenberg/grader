import random
import math
n=random.randint(1,20)
print("Bienvendo al programa de adivinacion, tiene 5 intentos para adivinar el numero que el programa ha elegido para usted \n el rango es del 1 al 20, Que tengas buena suerte")
intentos=1
while True:
    try:
        nu=int(input("Introduzca su numero: "))
        break
    except ValueError:
        print("Debe ser numerico")
while intentos<5:
    if(n==nu):
        break
    else:
        print("Lamentablemente no ha acertado, le quedan ",5-intentos," Intentos")
        if(nu>n):
            print("Una pista, su numero era mayor que mi numero")
        else:
            print("Una pista, su numero era menor que mi numero")
        while True:
            try:
                nu = int(input("Introduzca su nuevo numero: "))
                break
            except ValueError:
                print("Debe ser numerico")
        intentos=intentos+1
if(n==nu):
    print("Adivinaste, mi número era ",n)
else:
    print("No adivinaste, mi número era ",n)