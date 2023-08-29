##Juego adivina mi numero
from random import randint as r
numero = r(1,20)
intentos = 1
intento = 21
while intentos <= 5 and intento != numero :
    intento = int(input("Intenta advinar mi número: "))
    if intento > numero:
        print("Mi número es menor")
    elif intento < numero:
        print("Mí número es mayor")
    intentos = intentos + 1

if intento == numero:
    print("Adivinaste, mi número era {}".format(numero))
if intento != numero:
    print("No adivinaste, mi número era {}".format(numero))