import random
n=random.randint(1,20)
i=0
while i<5:
    a=int(input())
    i+=1
    if a==n:
        print("Adivinaste, mi número era ",a)
        break
    elif a>n:
        print("El número ingresado es mayor")
    else:
        print("El número ingresado es menor")
if i==5:
    print("No adivinaste, mi número era ",n)