#Juego adivina mi número
import random

intentos = 0
MinMumero = 1
MaxNumero = 20
#Numero Random
Numero = random.randint(MinMumero,MaxNumero)
#Condicion
while intentos < 5:
    Num=int(input("Ingrese un numero entre 1 y 20:"))
#Ciclo While
    intentos = intentos + 1

    if Num < Numero:
        print("mi numero es menor")
    if Num > Numero:
        print("mi numero es mayor")
    if Num == Numero:
        break

if Num == Numero:
    intentos = str(intentos)
    print("Adivinaste, mi número era:",Numero )
else:
    if Num != Numero:
        print("No adivinaste, mi número era:",Numero)    