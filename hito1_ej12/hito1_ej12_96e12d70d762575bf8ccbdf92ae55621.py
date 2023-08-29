#Juego adivina mi número

import random
random=random.randint(1,20)
b=int(input("entre el 1 y 20, ¿en que numero estoy pensando?: "))
intentos=1

while b!=random and intentos<5 :
    if b>random :
        print("mi numero es menor")
        b=int(input("entre el 1 y 20, ¿en que numero estoy pensando?: "))
        intentos=intentos+1
    elif b<random :
        print("mi numero es mayor")
        b=int(input("entre el 1 y 20, ¿en que numero estoy pensando?: "))
        intentos=intentos+1

if intentos==5 and b!=random:
    print("no adivinaste, mi numero era ",random)

if b==random and intentos<=5:
    print("adivinaste, mi numero era ",random)