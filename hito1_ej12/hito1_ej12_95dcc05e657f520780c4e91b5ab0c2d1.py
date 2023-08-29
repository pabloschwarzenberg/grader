#Juego adivina mi número
import random
Numeroaleatorio=random.randint(1,20)
numerointentos= 5 
while numerointentos != 0:
    numerousuario=int(input("Ingrese un numero "))
    if numerousuario < Numeroaleatorio:
        print("tu numero es menor")
    elif numerousuario > Numeroaleatorio :
        print("Tu numero es mayor")
    if numerousuario != Numeroaleatorio:
        numerointentos=numerointentos-1
    elif numerousuario == Numeroaleatorio:
        print("Adivinaste, mi numero era:",Numeroaleatorio)
        break
if numerointentos == 0:
    print("No adivinaste,mi numero era:",Numeroaleatorio)    