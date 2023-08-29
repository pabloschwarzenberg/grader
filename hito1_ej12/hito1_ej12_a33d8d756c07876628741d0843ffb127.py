#Juego adivina mi número
from random import randint
condicion=True
contador=0
numero=randint(1,20)
while condicion:
    x =eval(input("adivina mi numero: "))
    if x==numero:
        print("Adivinaste, mi número era", numero)
        break

    if x>numero:
        contador = contador + 1
        print("mi número es menor")

    if x<numero:
        print("mi número es mayor")
        contador = contador + 1

    if contador==5 :
        print("No adivinaste, mi número era", numero)
        condicion = False