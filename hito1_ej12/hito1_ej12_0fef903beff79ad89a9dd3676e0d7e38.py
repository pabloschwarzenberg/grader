import random 
numsecreto=random.randint(1,20)

usuario=int(input("Ingrese el numero:"))

contador=1
for i in [0,1,2,3,4,5]:
    if numsecreto<usuario:
        print("Mi número es menor")
    if numsecreto>usuario:
        print("Mi numero es mayor")
    usuario=int(input("Ingrese otro numero:"))    
    contador=contador+1
    if contador==5:
        print("No adivinaste, mi número era",numsecreto)
        break
    if numsecreto==usuario:
        print("Adivinaste, mi numero era",numsecreto)
        break