#Juego adivina mi número
#Adivina Mi numuero
import random
secreto= random.randint(1,20)
i=1
while i<6:
    print("Intento N°",i)
    valor= int(input("Ingresa un Numero: "))
    if valor == secreto:
        print ("Felicitaciones has Acertado mi numero es :", secreto)
        i=6
    if valor < secreto:
        print ("Tu Numero es Menor que el Numero Secreto")
        i=i+1
    if valor > secreto:
        print ("Tu Numero es Mayor que el Numero Secreto")
        i=i+1
if valor != secreto:
    print("Se acabaron tus Intentos El numero Secreto es: ", secreto)