#Juego adivina mi número
numero_oculto = 13
intentos_del_jugador = 5
numero_jugador = ""
while(numero_jugador == ""):
    numero_jugador = eval(input("ingresa un numero:"))
    if(numero_jugador != numero_oculto):
        intentos_del_jugador = intentos_del_jugador - 1
        if(intentos_del_jugador == 0):
            print("No adivinaste, mi número era", numero_oculto)
        elif(numero_jugador > numero_oculto):
            print("mi numero es menor")
            numero_jugador = ""
        elif(numero_jugador < numero_oculto):
            print("mi numero es mayor")
            numero_jugador = ""
    elif(numero_jugador == numero_oculto):
        print("Adivinaste, mi número era", numero_oculto)     