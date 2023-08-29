#Juego adivina mi número
from random import randrange, choice

secreto= (randrange(1, 20))


intentos = 0
while intentos <5 :
     numero = float(input("Ingresa un numero entre el 1 y el 20: "))
     intentos = intentos + 1
     if numero > secreto:
        print("Mi numero es menor")
     if numero < secreto:
        print("Mi numero es mayor")
        

if numero == secreto:
     print("Adivinaste, mi numero era: ",secreto)
if numero != secreto:
     print("No adivinaste, mi número era ", secreto)
     
