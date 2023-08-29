#Juego adivina mi número
import random
npc=random.randint(1,20)
nu=int(input("Ingrese número: "))
contador=0
while contador<4:
    if nu<npc:
        print("El número es mayor")
        contador=contador+1
        nu=int(input("Ingrese nuevamente: "))
    elif nu>npc:
        print("El número es menor")
        contador=contador+1
        nu=int(input("Ingrese nuevamente: "))
    elif nu==npc:
        print("Adivinaste! el número era "+str(npc))
        break
if contador==4:
    if nu!=npc:
        print("No adivinaste, el número era "+str(npc))
    elif nu==npc:
        print("Adivinaste! el número era "+str(npc)) 
    
    
