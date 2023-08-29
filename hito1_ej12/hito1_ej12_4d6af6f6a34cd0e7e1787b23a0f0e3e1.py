#Juego adivina mi número
import random
aleatorio=random.choice(range(20))
aleatorio=int(aleatorio)

numero=int(input("Ingrese número:"))
contador=1
while contador<5:
    
    if numero>aleatorio:
        print("menor")
        numero=int(input("Ingrese número:"))

    if numero<aleatorio:
        print("mayor")
        numero=int(input("Ingrese número:"))

    contador+=1

    if numero==aleatorio:
        print("Adivinaste, mi número era",aleatorio)
        break
        
if contador==5 and numero!=aleatorio:
    print("No adivinaste, mi número era",aleatorio)  