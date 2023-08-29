#Adivina mi numero :3
import random
n=random.randint(1,20)
intentos=5
while intentos>=1:
    intentos-=1
    gg=int(input("Adivina mi numero [Pista:Está entre el 1 y el 20]: "))
    if gg<n:
        print("Nop, mi número es mayor a eso! :/")
        print("Te quedan",intentos,"intentos para adivinar mi numero!")
        
    elif gg>n:
        print("Nop, es menor! xD")
        print("Te quedan",intentos,"intentos para adivinar mi numero!")
       
    elif gg==n:
        print("Wena!, adivinaste mi numero, siéntete feliz y dile a tus papás :3")
        break
if intentos==0 and n!=gg:
        print("Que sad ;-;, mi número era",n)

