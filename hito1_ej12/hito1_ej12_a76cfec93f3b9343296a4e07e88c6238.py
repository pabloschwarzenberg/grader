#Juego adivina mi número
from random import randint


intentos=5
num_aleatorio=randint(1,20)
num=0
while intentos>0 and num!=num_aleatorio:
    num=int(input("adivina el numero: "))
    if num<num_aleatorio:
        print("mi número es mayor")
        intentos=intentos-1
    elif num>num_aleatorio:
        print("mi número es menor")
        intentos=intentos-1
    elif num==num_aleatorio:
        break
if num == num_aleatorio:        
    print("Adivinaste, mi número era",(num_aleatorio))
else:
    print("No adivinaste, mi numero era",(num_aleatorio))