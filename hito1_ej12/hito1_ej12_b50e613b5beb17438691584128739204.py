#Juego adivina mi número
import random

computador=random.randint(1,20)

i=0
while i<=4:
    persona=int(input("Intente adivinar un numero entre el 1 y el 20:"))
    i=i+1
    if persona==computador:
        print("Adivinaste, mi numero era",computador)
        break
    elif persona < computador:
        print("Fallaste, el numero es mayor al que ingresaste")

    elif persona > computador:
        print("Fallaste, el numero es menor al que ingresaste")
    if i>4:
       print("No adivinaste, mi numero era",computador)