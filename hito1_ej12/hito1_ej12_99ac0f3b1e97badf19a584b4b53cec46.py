#Juego adivina mi númeronumero_secreto= 13
numero_secreto= 19
intentos=5
numero_jugador=""
while(numero_jugador==""):
    numero_jugador=eval(input("ingresa un numero:"))
    if(numero_jugador!=numero_secreto):
        intentos=intentos-1
        if(intentos==0):
            print("No adivinaste, mi número era", numero_secreto)
        elif(numero_jugador>numero_secreto):
            print("elije un numero es menor")
            numero_jugador=""
        elif(numero_jugador<numero_secreto):
            print("elije un numero es mayor")
            numero_jugador=""
    elif(numero_jugador==numero_secreto):
        print("Acertaste, mi número era", numero_secreto)