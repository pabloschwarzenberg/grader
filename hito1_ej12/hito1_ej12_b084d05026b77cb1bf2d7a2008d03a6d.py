#Juego adivina mi número
import random
a=random.randint(1, 20)
intentos=0    
while intentos<=5:
    b=int(input("Ingresa un número:"))
    if b==a:
        print ("Adivinaste, mi número era",a)
        break
    else:
        intentos= intentos+1
        if b>a:
            print("Mayor")
        elif b<a:
            print("Menor")
        if intentos==5 and b!=a:
            print("No adivinaste, mi número era",a)
            break
          