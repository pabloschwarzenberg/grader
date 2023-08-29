#Juego adivina mi número
import random
minumero=random.randint(1,20)
print(minumero)
i=0
while i<5:
    sunumero=int(input("Ingrese un número del 1 al 20: "))
    if minumero==sunumero:
        print("Adivinaste, mi número era ", minumero)
        break
    elif(minumero<sunumero):
        print("Mi numero es menor")
        i=i+1
    else:
        print("Mi numero es mayor")
        i=i+1     