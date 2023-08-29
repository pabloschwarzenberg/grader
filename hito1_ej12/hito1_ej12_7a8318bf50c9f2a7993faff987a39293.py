#Juego adivina mi número
import random
veces=1
pc=random.randint(1,20)
num=int(input("Ingrese un numero: "))
while veces<=5:
    if num>pc:
        print("Ingresa un numero menor")
    elif num<pc:
        print("Ingresa un numero mayor")
    elif num==pc:
        print("Lo adivinaste, mi numero era:",pc)
        break
    veces=veces+1
    num=int(input("Ingrese un numero: "))
if num!=pc:
     print("No adivinaste, mi numero era:",pc)