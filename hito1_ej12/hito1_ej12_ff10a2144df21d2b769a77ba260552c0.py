import random
numero=random.randint(1,20)

intentos=5
while intentos>0:
    n=int(input())
    if n<numero:
        print("Mi número es mayor")
        intentos=intentos-1
        continue
    elif numero<n:
        print("Mi número es menor")
        intentos=intentos-1
        continue
    else:
        print("Adivinaste, mi número era",numero)
        break
if intentos==0:
    print("No adivinaste, mi número era",numero)