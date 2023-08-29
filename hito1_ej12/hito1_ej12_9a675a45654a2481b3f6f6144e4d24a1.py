#Juego adivina mi número
intentos = 5
secreto = 15
jugador = 0
intentos_jugador = 1

while ((intentos_jugador <= 5) and (jugador != 15)):
    jugador = int(input("Ingrese un número: "))
    if(intentos_jugador == 5):
        print("No adivinaste, mi número era 15")
    elif(jugador > secreto):
        print("Mi numero es menor")
    elif(intentos_jugador == 5):
        print("No adivinaste, mi número era 15")
    elif(jugador < secreto):
        print("Mi numero es mayor")    
    intentos_jugador = intentos_jugador + 1
if(jugador == secreto):
        print("Adivinaste, mi número era 15")
