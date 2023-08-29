#Juego adivina mi número
import random
numero = random.randint(1,20)

opo = 5
for i in range(5):
    opcion = int(input("Ingrese su Numero"+str(i+1)+":"))
    if numero==opcion:
        print("Adivinaste, mi numero era" + str(numero))
        break
    elif opcion<numero:
        print("Mi numero es Mayor")
    elif opcion>numero:
        print("Mi numero es Menor")
    if i ==4:
        print("No Adivinaste, mi Numero era" +str(numero))    