import random
x=int(input())
el_random=random.randint(1,20)
intentos=1
while intentos<=5:
    z=int(input())
    if intentos==5:
        print("No adivinaste, mi número era",el_random)
    else:
        if z>el_random:
            print("mi número es menor")
            intentos+=1
        if z<el_random:
            print("el número es mayor")
            intentos+=1
        if z==el_random:
            print("adivinaste, mi número era",el_random)