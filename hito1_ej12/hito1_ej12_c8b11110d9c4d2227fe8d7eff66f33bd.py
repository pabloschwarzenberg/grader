#Juego adivina mi número
import random

numero_aleatorio = random.randint(1,20)
print(numero_aleatorio)

intentos = 0

while(intentos <5):

    numero_ingresado=int(input("intenta adivinar el numero"))
    
    intentos =  intentos + 1
    print("llevas",intentos,"intentos")
    if(numero_ingresado == numero_aleatorio):
        print( "Adivinaste, mi número era ",numero_aleatorio)
        break 

    elif(numero_aleatorio > numero_ingresado):
        print("Tu numero ingresado es menor")
    elif(numero_aleatorio < numero_ingresado):
        print("tu numero ingresado es mayor")

if(numero_aleatorio!= numero_ingresado ):
    print("No adivinaste, mi número era ",numero_aleatorio)

    

