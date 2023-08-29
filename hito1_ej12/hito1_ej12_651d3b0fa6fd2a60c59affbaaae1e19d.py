from random import randint, uniform,random
a=int(randint(1,20))
i=0
while i<5:
    b=int(input())
    if a<b:
        print("mi número es menor")
    if a==b:
        print("Adivinaste mi número era ",a)
        break
    if a>b:
        print("mi número es mayor")
    i=i+1
if i==5:
    print("No adivinaste, mi número era ",a)