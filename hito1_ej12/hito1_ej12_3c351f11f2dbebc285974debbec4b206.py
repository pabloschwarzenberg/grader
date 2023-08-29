#Juego adivina mi número
import random

numero=random.randint(1,20)          
intentos=0

jugando= True
print("Adivina un Nùmero del 1 al 20")
while jugando:
    
        intentos+=1
        
        if intentos <=5:
            eleccion = int(input("Dime un numero:"))
            if eleccion == numero:
                print("Adivinaste, mi numero era "+ str(numero))
                jugando= False
            elif eleccion > numero:
                print("mi número es mayor")
            elif eleccion < numero:
                print("mi número es menor")
        else:
            print("No adivinaste, mi número era "+ str(numero))
            jugando= False
      