from random import randint
a=0
n=randint(1,20)
c=0
while a<5:
    b=int(input("ingresa un número:"))
    if b==n:
        c=1
        a=5
    elif b<n:
        print("Ingresaste un número menor")
        a=a+1
    else:
        print("Ingresaste un número mayor")
        a=a+1
if c==1:
    print("Adivinaste, mi número era",n)
else:
    print("No adivinaste, mi número era",n)