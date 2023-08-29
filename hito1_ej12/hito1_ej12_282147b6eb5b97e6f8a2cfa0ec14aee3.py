from random import randint

n = randint(1,20)
print(n)
intentos=0

while intentos<5:
    nUser = int(input("Ingrese un número:"))
    if intentos<4:
        if nUser>n:
            print("mi número es menor")
            intentos=intentos+1
        elif nUser<n:
            print("mi número es mayor")
            intentos = intentos + 1
        else:
            print("Adivinaste, mi número era ",n)
            break
    else:
        print("No adivinaste, mi número era ",n)
        break
      