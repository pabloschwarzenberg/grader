#Juego adivina mi número
import random
num=random.randint(1,20)
intentos=5

while intentos>0:
    mi_num=int(input())
    if mi_num==num:
        print("Adivinaste, mi numero era",num)
        break
    elif mi_num<num:
        print("Mi numero es mayor")
        intentos-=1
    elif mi_num>num:
        print("Mi numero es menor")
        intentos-=1

if intentos==0:
    print("No adivinaste, mi numero era ",num)
