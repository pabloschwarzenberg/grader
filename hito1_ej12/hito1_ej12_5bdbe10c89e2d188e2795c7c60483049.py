#Juego adivina mi número
numero_secreto= 13
intentos=5
numero_jugador=""
while(numero_jugador==""):
    numero_jugador=eval(input("ingresa un numero:"))
    if(numero_jugador!=numero_secreto):
        intentos=intentos-1
        if(intentos==0):
            print("No adivinaste, mi número era", numero_secreto)
        elif(numero_jugador>numero_secreto):
            print("mi numero es menor")
            numero_jugador=""
        elif(numero_jugador<numero_secreto):
            print("mi numero es mayor")
            numero_jugador=""
    elif(numero_jugador==numero_secreto):
        print("Adivinaste, mi número era", numero_secreto)