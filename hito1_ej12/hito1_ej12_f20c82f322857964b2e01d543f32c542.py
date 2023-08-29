#Juego adivina mi número
import random
numero_random=random.randint(1,20)
numero1=numero_random
i=1
while i<=5:
    numero=int(input("ingrese un numero: "))
    if numero>numero1:
        print("mi numero es menor")
    elif numero<numero1:
        print("mi numero es mayor")
    elif numero1==numero:
        print("adivinaste , mi numero",numero1)
    else:
        print("no adivino")
    i=i+1     