#Juego adivina mi número
import random
numero= random.randint(1,20)
print("Ingrese el numero que cree usted que es: ")
eleccion=0
cont =1
while cont < 6 and eleccion != numero:
    eleccion=int(input("-->"))
    if eleccion<numero:
        cont=cont+1
        print("El numero es mayor al que pusiste")
        
    if eleccion>numero:
        cont=cont+1
        print("El numero es menor al elejido")
    if eleccion == numero:
        print("Adivinaste, mi numero era",numero)
        break

    if cont==6:
        print("No adivinaste,mi numero era",numero)
