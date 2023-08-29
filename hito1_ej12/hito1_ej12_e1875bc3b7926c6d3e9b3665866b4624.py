import random
a=random.randint(1,20)
b=int(input())
Nint=0
while a!=b :
    if a<b:
        print("mayor")
        Nint=Nint+1
        b=int(input())
    if a>b:
        print("menor")
        Nint=Nint + 1
        b=int(input())
    if Nint==4:
        print("No adivinaste, mi número era",a)
        break
if (a==b) :
    print("Adivinaste, mi número era",a)