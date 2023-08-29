import random

n=random.randrange(1,21)

for i in range(0,5):
    a=int(input())
    if a==n:
        print("Adivinaste, mi número era ",n)
        break
    elif a>n:
        print("El número es menor")
    elif a<n:
        print("El número es mayor")
    if i==4:
        print("No adivinaste, mi número era ",n)