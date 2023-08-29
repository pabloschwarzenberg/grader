import random
pc=random.choice(range(20))
pc=int(pc)
contador=1
print("Adivine el numero, del 1 al 20 :)")

while contador<=5:
    N=int(input("Ingrese numero:"))
    if N==pc:
        print("Adivinaste, mi numero era",pc)
        break
    
    else:
        if N>pc:
            print("mayor")
        if N<pc:
            print("menor")
        
        contador+=1

if contador==6:
    print("No adivinaste, mi numero era",pc)