#Juego adivina mi número
import sys
import random
# Numero secreto
numero_secreto=random.randint(1,20)
intentos=0
while(intentos<5):
    numero_ingresado=int(input("Adivina mi numero: "))
    if(numero_ingresado<numero_secreto):
        print("El numero que has ingresado es menor que mi numero")
        intentos=intentos+1
    elif(numero_ingresado>numero_secreto):
        print("El numero que has ingresado es mayor que mi numero")
        intentos=intentos+1
    else:
        print("Adivinaste, mi número era",numero_secreto)
if(intentos==5):
    print("No adivinaste, mi número era",numero_secreto)