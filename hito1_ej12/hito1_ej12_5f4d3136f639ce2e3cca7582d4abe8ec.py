#Juego adivina mi número
import random
numero=random.randrange(21)
intentos=0
while(intentos<5):
    jugador=int(input("ingrese un numero: "))
    if (jugador == numero):
        print("adivinaste mi numero era", numero)
        intentos=5

    elif(numero<jugador):
        print("tu numero es mayor al numero secreto")
    elif(numero>jugador):
        print("tu numero es menor al numero secreto")
    intentos+=1
if(intentos==5):
    print("no adivinaste mi numero era",numero)      