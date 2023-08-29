#Juego adivina mi número
from random import randint
aleatorio=randint(1,20)
turno=1
while turno<=5:
    num=int(input("Adivina mi número: "))
    #adivinaste
    if  num==aleatorio:
        print("Adivinaste, mi número era",aleatorio)
        turno+=5
    #Numero menor
    elif num<aleatorio:
        if  turno==5:
            print("No adivinaste, mi número era",aleatorio)
            turno+=1
        elif turno<5:
            print("mi número es mayor")
            turno+=1
    #Numero mayor
    elif num>aleatorio:
        if  turno==5:
            print("No adivinaste, mi número era",aleatorio)
            turno+=1
        elif turno<5:
            print("mi número es menor")
            turno+=1