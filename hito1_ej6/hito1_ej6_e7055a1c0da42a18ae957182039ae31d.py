#Ordenar tres números
   #Ordenar tres números
from os import system
system("cls")

lista=[]
n1 = int(input("Ingrese el primer numero: "))
lista.append(n1)
n2 = int(input("Ingrese el segundo numero: "))
lista.append(n2)
n3 = int(input("Ingrese el tercer numero: "))
lista.append(n3)

lista.sort()
print(lista)   