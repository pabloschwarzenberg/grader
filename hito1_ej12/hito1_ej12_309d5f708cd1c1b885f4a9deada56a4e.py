#Juego adivina mi número
import random
secreto=random.randint(1, 20)
intentos=0
acerto="N"
while (intentos < 5):
    num=int(input("ingrese numero a adivinar: "))
    intentos+=1
    if(num==secreto):
        acerto="S"
        break
    else:
        if(num<secreto):
            print("Mi numero es mayor")
        else:
            if(num>secreto):
                print("Mi numero es menor")

if(acerto=="S"):
    print("Adivinaste, mi numero era",secreto)
else:
    print("No adivinaste, mi número era :",secreto)      