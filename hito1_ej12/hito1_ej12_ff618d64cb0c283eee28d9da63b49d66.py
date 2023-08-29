#Juego adivina mi número
import random

b=random.randint(1,20)

i=1

while i<6:
    a=int(input("Ingresa un numero: "))
    if(a==b):
      print("Adivinaste, mi número era",b)
      break
    elif(a<b):
      print("El número ingresado es menor")
      i=i+1
    elif(a>b):
      print("El número ingresado es mayor")
      i=i+1

if(i==6):
    print("No adivinaste, mi número era ",b)

