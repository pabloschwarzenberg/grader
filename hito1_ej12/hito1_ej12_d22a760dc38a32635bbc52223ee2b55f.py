#Juego adivina mi número
import random 
def adivina(secreto,num): 
    while True:
        if num == secreto:
            print("¡ESE ERA!... ganaste!")
        elif num < secreto: 
            print("El número que buscas es más alto...")
        else:   
            print("El número que buscas es más bajo...") 
        return num 
secreto = random.randint(1,20)
num = 5
print(adivina(secreto,num))     