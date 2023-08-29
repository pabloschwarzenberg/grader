#Juego adivina mi número
import random

numero = eval(input("Ingrese el número:"))

numero_secreto = random.randint(1,100)

while numero != numero_secreto:
    if numero < numero_secreto:
        print ( "Tu número es Menor" )
    else:
        print ( "Tu número es Mayor" )
        
    numero = eval(input("Ingrese el número:"))

print("Felicidades el número es:",numero_secreto)