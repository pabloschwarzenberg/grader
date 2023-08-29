#Juego adivina mi número
import random
while True:
    numero = int(input("Ingrese un numero"))
    secreto = random.randint(1,20)
    if numero == secreto:
        
        print("Adivinaste, mi número era ", secreto)

    if numero != secreto:
        if numero > secreto:
            print("mi número es menor")
        if numero < secreto:
            print("mi número es mayor")
        print("Intento N°2")
        
        numero = int(input("Ingrese un numero"))
        if numero != secreto:
            if numero > secreto:
                print("mi número es menor")
            if numero < secreto:
                print("mi número es mayor")
            print("Intento N°3")
            
            numero = int(input("Ingrese un numero"))
            if numero != secreto:
                if numero > secreto:
                    print("mi número es menor")
                if numero < secreto:
                    print("mi número es mayor")
                print("Intento N°4")
                
                numero = int(input("Ingrese un numero"))
                if numero != secreto:
                    if numero > secreto:
                        print("mi número es menor")
                    if numero < secreto:
                        print("mi número es mayor")
                    print("Intento N°5")
                    print("No adivinaste, mi número era ",secreto)
                    
                    break