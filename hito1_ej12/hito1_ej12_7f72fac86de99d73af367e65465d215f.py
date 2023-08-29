#Juego adivina mi número
from random import randint
numero=randint(1,20)
intentos=1
while intentos<5 or respuesta==numero:
    respuesta=int(input("ingrese numero: "))
    if numero<respuesta:
        print("mi numero es menor")
    if numero>respuesta:
        print("mi numero es mayor")
    if numero==respuesta:
        print("adivinaste, mi numero era",numero)
        break
    intentos+=1
    
if intentos==5:
    respuesta=int(input("ingrese numero: "))
    if numero==respuesta:
        print("adivinaste, mi numero era",numero)
    else:
        print("no adivinaste, mi numero era",numero)    