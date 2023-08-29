#Juego adivina mi numero
import random
numero= random.randint(1,20)
oportunidad=0
fallo = 0

while True:
    if fallo < 5:
        oportunidad = int(input("numero: "))
        fallo = fallo + 1
        if oportunidad != numero and fallo<5:
            if oportunidad < numero:
                print("El numero secreto es mayor:")
            else:
                print("El numero secreto es menor:")
            
        elif oportunidad == numero:
            print("Adivinaste, era", numero)
            break
    elif fallo == 5:
        print("No adivinaste, era",numero)
        break