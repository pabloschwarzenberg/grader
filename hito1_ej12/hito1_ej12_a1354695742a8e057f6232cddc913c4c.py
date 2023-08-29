from random import randint
r=(randint(1,20))
n=int(input())
if n==r:
    print("Adivinaste, mi número era ",n)
    exit
if n>r:
    print("mi numero es menor")
elif n<r :
    print("mi numero es mayor")
m=int(input())
if m==r:
    print("Adivinaste, mi número era ",m)
    exit
if m>r:
    print("mi numero es menor")
elif m<r :
    print("mi numero es mayor")
b=int(input())
if b==r:
    print("Adivinaste, mi número era ",b)
    exit
if b>r:
    print("mi numero es menor")
elif b<r :
    print("mi numero es mayor")
v=int(input())
if v==r:
    print("Adivinaste, mi número era ",v)
    exit
if v>r:
    print("mi numero es menor")
elif v<r :
    print("mi numero es mayor")
c=int(input())
if c==r:
    print("Adivinaste, mi número era ",c)
    exit
else:
    print("No adivinaste, mi número era ",r)
    exit
    