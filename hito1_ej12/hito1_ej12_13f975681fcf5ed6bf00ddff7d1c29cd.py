#Juego adivina mi número
import random
numero=random.randint(1,20)
conteo=0
while(conteo<5):
    conteo=conteo+1
    A=int(input("ingresar numero"))
    if(numero==A):
        print("Adivinaste, mi numero era",numero)
        break
    if(A<numero):
        print("tu numero es menor que el numero secreto")
    if(A>numero):
        print("tu numero es mayor que el numero secreto")
    
if(conteo==5):
        print("No adivinaste mi numero era",numero)
  
