#Juego adivina mi número
from random import randint

Numero = randint(1,20)

con = 5
for i in range(5):
    opcion = int(input("Ingrese su Numero"+str(i+1)+":"))
    if Numero==opcion:
        print("Adivinaste, mi numero era" + str(Numero))
        break
    elif opcion<Numero:
        print("Mi numero es Mayor")
    elif opcion>Numero:
        print("Mi numero es Menor")
    if i ==4:
        print("No Adivinaste, mi Numero era" +str(Numero))