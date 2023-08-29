#Juego adivina mi número
import random

def  inicio():
    numrandom= random.randint(1,20)
    numero,confirmacion=juego(numrandom)
    if confirmacion==True:
        print("Adivinaste, mi numero era %s" %(str(numero)))
    elif confirmacion==False:
        print("No adivininaste, mi numero era %s" %(str(numero)))

def juego(nrandom):
    for i in range(5):
        intento= int(input("Ingrese intento: "))
        if intento == nrandom:
            return intento, True
        elif intento < nrandom:
            print("mi numero es mayor")
        elif intento > nrandom:
            print("mi numero es menor")
    return 0,False
    
inicio()  