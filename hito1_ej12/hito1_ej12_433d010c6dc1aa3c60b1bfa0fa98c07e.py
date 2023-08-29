#Juego adivina mi número
numero_secreto=6
numero_jugador=0
intentos=5

while((numero_jugador !=numero_secreto) and (intentos>0)):
    numero_jugador= eval(input("Ingrese número: "))

    if(numero_jugador > numero_secreto):
        print("Mi numero es menor.")
    elif(numero_jugador < numero_secreto):
        print("Mi numero es mayor.")

    intentos-=1

if(numero_jugador==numero_secreto):
    print("Adivinaste, mi numero era: ", numero_secreto)
else:
    if(intentos==0):
        print("No adivinaste, mi número era: ",numero_secreto)
              
    

              

    