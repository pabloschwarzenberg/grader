import random
a=random.randint(1,20)
intentos=4
b=int(input())
while intentos>=1:
    while b > a:
        intentos=intentos-1
        print("El numero es menor")
        b=int(input())
        break
    while b < a:
        intentos=intentos-1
        print("El numero es mayor")
        b=int(input())
        break
    while b==a:
        print("Adivinaste, mi numero era",a)
        break
else:
    print("No adivinaste, mi numero era",a)