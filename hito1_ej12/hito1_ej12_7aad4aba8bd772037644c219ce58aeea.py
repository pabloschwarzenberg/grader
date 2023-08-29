#Juego adivina mi número
from random import randint

NumeroAdivinar = randint(0,21)
Intentos = 0
while Intentos < 5:
    Numero = int(input("Ingrese el numero que a adivinar >>> "))
    if Numero != NumeroAdivinar and Numero < NumeroAdivinar:
        Intentos += 1
        print("Incorrecto", Numero , "es menor al numero que debe adivinar")
    elif Numero != NumeroAdivinar and Numero > NumeroAdivinar:
        Intentos += 1
        print("Incorrecto,",Numero,"es mayor al numero a adivinar")
    
    elif Numero == NumeroAdivinar:
        Intentos += 5
        print("Correcto, el numero era ",NumeroAdivinar)
print("El numero a adivinar era ",NumeroAdivinar,)