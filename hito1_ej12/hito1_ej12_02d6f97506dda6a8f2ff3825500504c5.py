intentos = 1
import random
n= int(input("ingrese un numero"))

numero_oculto= random.randint(1,20)

if n == numero_oculto:
    print ("Adivinaste, mi número era",numero_oculto)
    
else:
    while n!= numero_oculto:
        if intentos < 5:
            if n < numero_oculto:
                print ("mi numero es mayor")
                n= int(input("ingrese un numero"))
                intentos+=1
        
            elif n > numero_oculto:
                print ("mi numero es menor")
                n= int(input("ingrese un numero"))
                intentos+=1

            elif n == numero_oculto:
                print ("Adivinaste, mi número era",numero_oculto)

        else:
            print ("No adivinaste, mi número era",numero_oculto)
            break
