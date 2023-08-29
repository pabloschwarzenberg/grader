#Juego adivina mi número
from random import randint
numero = randint(1, 20)

contador = 1
while contador <= 5 :
    adivinar = eval(input("ingresa el numero: "))
    if adivinar < numero :
        print("mi numero es mayor")
        contador += 1
        continue
    if adivinar > numero :
        print("mi numero es mayor")
        contador += 1
        continue
    if adivinar == numero :
        print("Adivinaste mi numero, mi numero era:", numero)
        break