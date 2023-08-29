#Juego adivina mi número
import random as rm 

numero = rm.randrange(20)
resp = 0
i=0

while i < 5:
    resp = int(input("ingrese el numero que cree que es"))
    
        

    if i == 5: 
        
        print("No adivinaste, mi número era",numero)
        break
    
    elif resp > numero:
        print("Mi número es menor")
        i = i + 1
    elif resp == numero:
        print("Adivinaste mi número era",numero)
        break
    elif resp < numero:
        print("Mi número es mayor")
        i = i + 1  
        
        
    else:
        break





