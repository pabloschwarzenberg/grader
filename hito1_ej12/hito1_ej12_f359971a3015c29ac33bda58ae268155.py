#Juego adivina mi número
import random
numero = random.randint(1,20)
intentos = 0
while intentos <= 5 :
    intentos=intentos+1
    seleccion = int(input("Adivine el numero: "))
    if seleccion<numero:
        print("El numero secreto es mayor")
    elif seleccion>numero:
        print("El numero secreto es menor")
    if seleccion==numero:
        print("Adivinaste mi numero era",numero)
        break
    if intentos==5:
        print("No adivinaste, mi numero era", numero)
        break
