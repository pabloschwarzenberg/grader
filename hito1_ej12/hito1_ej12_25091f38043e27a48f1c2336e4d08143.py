#Juego adivina mi número
import random
computador=random.randint(1,20)
i=0
while i<5:
    numero=int(input("numero del 1 al 20 "))
    if (computador==numero):
        print("ganaste")
        break
    elif (i==5):
        print("perdiste")
        break
    elif (computador>numero):
        print("el numero es mayor")
        i+=1
    elif (computador<numero):
        print("el numero es menor")
        i+=1
    

      