#Juego adivina mi número
import random
numerosecreto=random.randint(0,20)
print(numerosecreto)
numero=int(input("ingrese un numero: "))
cuentaintentos=2

while not cuentaintentos>5 and numerosecreto!=numero:
    if numero<numerosecreto:
        print("mi numero es mayor")
        numero=int(input("ingrese numero: "))
        cuentaintentos=cuentaintentos+1
    if numero>numerosecreto:
        print("mi numero es menor")
        numero=int(input("ingrese numero: "))
        cuentaintentos=cuentaintentos+1
if numero==numerosecreto:
    print("adivinaste, mi numero era: ",numerosecreto)
if numero!=numerosecreto:
    print("no adivinaste, mi numero era: ",numerosecreto)
    
      