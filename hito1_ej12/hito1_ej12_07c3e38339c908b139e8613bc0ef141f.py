#Juego adivina mi número
import random
numerosecreto= random.randint(1,20)
intentos=0

while intentos<5:
    numeroingresado= int(input("A ver si le achuntas a mi numero: "))
    
    if numeroingresado<numerosecreto:
        print("Su numero es menor al secreto")
        intentos= intentos +1
        

    elif numeroingresado==numerosecreto:
        print("Adivinaste, mi numero era",+numerosecreto)
        break
    else:
        print("Su numero es mayor al secreto")
        intentos= intentos +1
        

if intentos==5:
    print("No adivinaste, mi numero era",+numerosecreto)      