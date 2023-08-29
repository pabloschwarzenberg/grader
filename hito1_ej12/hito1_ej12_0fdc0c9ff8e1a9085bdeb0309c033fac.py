import random

x = random.randrange(20)

print(x)

r = int(input("Ingrese numero secreto: "))

#Intento 1

if r == x:
    print("Adivinaste, mi número era: ",x)
    
else:
    if r < x:
        print("El numero es mayor")
    else:
        print("El numero es menor")
        
#Intento 2    
    
    r = int(input("Ingrese numero secreto: "))
    
    if r == x:
        print("Adivinaste, mi número era: ",x)
    
    else:
        if r < x:
            print("El numero es mayor")
        else:
            print("El numero es menor")
            
#Intento 3
        
        r = int(input("Ingrese numero secreto: "))
    
        if r == x:
            print("Adivinaste, mi número era: ",x)
    
        else:
            if r < x:
                print("El numero es mayor")
            else:
                print("El numero es menor")
                    
#Intento 4                    
                    
            r = int(input("Ingrese numero secreto: "))
    
            if r == x:
                print("Adivinaste, mi número era: ",x)
    
            else:
                if r < x:
                    print("El numero es mayor")
                else:
                    print("El numero es menor")
                        
#Intento 5                        
                        
                r = int(input("Ingrese numero secreto: "))
    
                if r == x:
                     print("Adivinaste, mi número era: ",x)
    
                else:
                     print("No adivinaste, mi número era: ",x)