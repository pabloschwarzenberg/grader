#Juego Adivina mi número
print("Bienvenido al juego")
import random
numero_secret = random.randint(1,20)
numero = int(input("Adivina mi numero: "))

if(numero == numero_secret):
    print("\n\nAdivinaste, mi número era",numero_secret)
else:
    if(numero > numero_secret):
        print("mi número es menor")
        numero = int(input("\nAdivina mi numero: "))
    elif(numero < numero_secret):
        print("mi número es mayor")
        numero = int(input("\nAdivina mi numero: "))
    if(numero == numero_secret):
        print("\n\nAdivinaste, mi número era",numero_secret)
    else:
        if(numero > numero_secret):
            print("mi número es menor")
            numero = int(input("\nAdivina mi numero: "))
        elif(numero < numero_secret):
            print("mi número es mayor")
            numero = int(input("\nAdivina mi numero: "))
        if(numero == numero_secret):
            print("\n\nAdivinaste, mi número era",numero_secret)
        else:
            if(numero > numero_secret):
                print("mi número es menor")
                numero = int(input("\nAdivina mi numero: "))
            elif(numero < numero_secret):
                print("mi número es mayor")
                numero = int(input("\nAdivina mi numero: "))
            if(numero == numero_secret):
                print("\n\nAdivinaste, mi número era",numero_secret)
            else:
                if(numero > numero_secret):
                    print("mi número es menor")
                    numero = int(input("\nAdivina mi numero: "))
                elif(numero < numero_secret):
                    print("mi número es mayor")
                    numero = int(input("\nAdivina mi numero: "))
                if(numero == numero_secret):
                    print("\n\nAdivinaste, mi número era",numero_secret)
                else:
                    print("No adivinaste, mi número era",numero_secret)