import random
import sys
x=random.randint(0,20)

intentos=0

while intentos<5:
    y = int(input())

    if y==x:
        print("Adivinaste, mi número era",x)
        sys.exit()

    else:
        if y < x:
            print("El numero es mayor que", y)

        elif y > x:
            print("El numero es menor que", y)

    intentos = intentos + 1

print("No adivinaste, mi número era",x)