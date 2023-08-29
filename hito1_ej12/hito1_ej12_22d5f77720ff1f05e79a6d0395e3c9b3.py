#Juego adivina el numero
numero_usuario = ""
numero_secreto = 9
numero_intentos = 0

while (numero_usuario!=numero_secreto):
    numero_usuario = int(input("Ingrese numero entre 1 y 20: "))
    numero_intentos = numero_intentos + 1

    if(numero_usuario > numero_secreto):
        print("Mi numero es menor: ")
    elif(numero_usuario < numero_secreto):
        print("Mi numero es mayor: ")


    else:
        print("Adivinaste,mi numero era 9: ","y lo lograste en",numero_intentos,"intento(s)")
    
