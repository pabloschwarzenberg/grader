#Juego adivina mi número
import random
a=random.randint(1,20)
intentos=5
while intentos != 0:
    num=int(input())
    if num ==a:
        print("Adivinaste, mi número era",a)      
    elif num>a:
        print("Tu numero es mayor")
        intentos=intentos-1
    
    elif num<a:
        print("Tu numero es menor")
        intentos=intentos-1
if intentos == 0:
    print("No adivinaste, mi número era",a)
    
    