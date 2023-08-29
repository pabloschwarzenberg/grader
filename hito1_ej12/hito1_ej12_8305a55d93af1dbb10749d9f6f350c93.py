#Juego adivina mi número
import random
num=random.randint(0,20)
vidas=5
numero=0
while vidas!=0:
    numero=int(input("Ingrese el numero que cree que es:"))
    if numero==num:
        print("Adivinaste, mi número era ",num)
        break
    elif numero>num:
        vidas=vidas-1
        print("mi numero es menor")
    elif numero<num:
        vidas=vidas-1
        print("mi numero es mayor")
if vidas==0:
    print("No adivinaste, mi número era: ",num)    