#Juego adivina mi número
import random
secreto = random.randint(1,21)
intentos=0
while 5>=intentos:
    numero=int(input("Adivine un numero del 1 al 20: "))
    intentos=intentos+1
    if numero==secreto:
        print("Adivinaste, mi número era",secreto)
        break
    if numero>secreto:
        print("mi número es menor")
    if secreto>numero:
        print("mi número es mayor")
    if intentos==5:
        print("No adivinaste, mi número era ",secreto)
        break      