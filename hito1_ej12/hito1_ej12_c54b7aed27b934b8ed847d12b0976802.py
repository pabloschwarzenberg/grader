#Juego adivina mi número
import random
n=random.randint(1, 21)
inte=0
adi=0
while inte!=5:
    adi=int(input("prueba con un num"))
    if adi==n:
        print ("Adivinaste, mi número era ",n)
        break
    elif adi<n:
        print ("el numero ingresado es menor q mi numero")
    elif adi>n:
        print ("el numero ingresado es mayor q mi numero")    
    inte=inte+1
if inte==5:
    print ("No adivinaste, mi número era",n)
