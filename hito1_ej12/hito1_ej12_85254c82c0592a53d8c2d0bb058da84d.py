#Juego adivina mi número
import random
na=random.randint(1,20)
n=int(input("Ingresa un número del 1 al 20:"))
i=0
while i<4:
    if n>na:
        print("mi número es menor")
        n=int(input("Ingresa un número del 1 al 20:"))
        i=i+1
        if n==na:
            print("Adivinaste, mi número era:",na)
            i=6
    if n<na:
        print("mi número es mayor")
        n=int(input("Ingresa un número del 1 al 20:"))
        i=i+1
        if n==na:
            print("Adivinaste, mi número era:",na)
            i=6
if i==4:
    print("No adivinaste, mi número era:",na)            
      