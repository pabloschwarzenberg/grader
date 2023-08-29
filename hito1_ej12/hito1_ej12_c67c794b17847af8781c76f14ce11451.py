#Juego adivina mi número
from random import randint
numero=randint(0,20)
intentos=0
print("estoy pensando en un numero del 1 al 20, ¿cual es?. ")
while intentos<5:
    print("intenta adivinar el numero, ¿cual es?: ")
    adivina= int(input())
    intentos=intentos+1
    
    if adivina<numero:
        print("mi numero es mayor")
    if adivina>numero:
        print("mi numeor es menor")
    if adivina == numero:
        break

if adivina==numero:
    print("Adivinaste, mi número era ", numero)
if adivina!=numero:
    print("No adivinaste, mi número era ",numero)     