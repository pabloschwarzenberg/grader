import random
a=random.randint(1,20)
i=0
while i<5:
    x=int(input("Ingrese número"))
    if x<a:
        print("Su numero es menor que el numero secreto")
        i=i+1
    elif x>a:
        print("Su numero es mayor que el número secreto")
        i=i+1
    else:
        print("Adivinaste, mi número era", a)
        break
if i==5:
    print("No adivinaste, mi número era", a) 