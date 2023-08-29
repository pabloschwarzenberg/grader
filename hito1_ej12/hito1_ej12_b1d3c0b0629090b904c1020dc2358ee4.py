#Juego adivina mi número
import random
n=random.randrange(1,20)

intentos = 1
while intentos < 6 :
    numero=int(input("Escoja un numero:"))
    if numero>n:
        print("Mi numero es menor")
    elif numero<n:
        print("Mi numero es mayor") 
    elif numero == n:
        print("Adivinaste, mi numero era",n)
        break
    intentos = intentos + 1
if intentos >= 6 :
    print ("No adivinaste, mi numero era", n)         