#Juego adivina mi número
import random
numero_secreto=random.randint(1,20)
intento = 0
while intento <5:
    num=int(input("Ingresa número: "))
    if numero_secreto==num:
        break
    elif num>numero_secreto:
        print("mi número es menor")
    else:
        print("mi número es mayor")
    intento+=1
if num==numero_secreto:
    print("Adivinaste, mi número era " + str(numero_secreto))
else:
    print("No adivinaste, mi número era " + str(numero_secreto))      