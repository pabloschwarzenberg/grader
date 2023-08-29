#Juego adivina mi número
import random
def adivina():
    secreto= random.randint(1,100)
    while True:
        num= int(input("Ingrese su intento -> ")) 
        if num== secreto:
            print("Ese era felicidades")
        return
            elif num<secreto:
                print("Mi numero es mayor")
            
            else:
                print("Mi numero es menor")
     

juego=adivina()
print(juego)      