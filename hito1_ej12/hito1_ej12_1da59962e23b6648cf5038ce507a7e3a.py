#Juego adivina mi número
import random
N=random.randint(1,20)
fallos=0
while fallos<5:
    print("¿Cual el número oculto?")
    x=int(input(""))
    if x==N:
        print("Adivinaste, mi número era",N)
        break
    if x<N:
       print("mi numero es mayor")
       fallos=fallos+1
    if N<x:
        print("mi numero es menor")
        fallos=fallos+1    