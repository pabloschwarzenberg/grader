#Juego adivina mi número
import random
n=random.randint(1,20)
print(n)
i=0
while i<5:
    N=int(input("inserta un numero"))
    if n<N:
        print("mayor")
    elif n>N:
        print("menor")
    elif n==N:
        print("adivinaste, mi numero era",n)
    i+=1

