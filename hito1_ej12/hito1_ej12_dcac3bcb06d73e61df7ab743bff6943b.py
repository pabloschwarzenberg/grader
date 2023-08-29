#Juego adivina mi número
import random
numero=int(random.randint(1,20))
intentos=5
while intentos>0:
    
    numero_jugador=input()
    if int(numero)>int(numero_jugador) :
        print("Tu número es menor")
    elif int(numero)<int(numero_jugador) :
        print("Tu número es mayor")
    elif int(numero_jugador)==int(numero) :
        print("Adivinaste, mi número era",numero)
    intentos=intentos-1
if intentos==0 :
        print("No adivinaste, mi número era",numero)