#Juego adivina mi número
import random
numero=random.randint(1,20)
i=0
while True:
    i+=1
    guess=int(input("ingrese un numero del 1 al 20:"))
    if guess<numero:
        print("el numero que buscas es mayor")
    elif guess>numero:
        print("el numero que buscas es menor")
    elif guess==numero:
        print("Adivinaste, mi número era ",numero)
        break
    if i == 5:
        print("No adivinaste, mi número era ",numero)
        break
