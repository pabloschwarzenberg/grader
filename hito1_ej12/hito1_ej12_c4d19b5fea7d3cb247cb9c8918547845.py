#Juego adivina mi número
import random
numero = random.randint(1,20)
i=0
while i<=5:
    jugador = int(input("Ingrese numero:"))
    i=i+1
    if(jugador == numero):
        print("Adivinaste, mi numero era",numero)
        break
    
    elif(jugador>numero):
        print("Mayor")
    elif(jugador<numero):
        print("Menor")
    if(i==5):
        print("No adivinaste, mi numero era",numero)
        break 