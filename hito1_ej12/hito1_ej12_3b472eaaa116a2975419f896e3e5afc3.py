#Juego adivina mi número
from random import randint
numsecreto=randint(1,20)
intentos=5
cont=1
gana=False
while cont<=intentos:
    numero=int(input("ingresa numero:"))
    if numero==numsecreto:
        gana=True
        break
    else:
        if numsecreto>numero:
            print("mi numero es mayor")
        else:
            print("mi numero es menor")
    cont+=1
if gana:
    print("Adivinaste, mi numero era",numsecreto)
else:
    print("No adivinaste mi numero era",numsecreto)
  