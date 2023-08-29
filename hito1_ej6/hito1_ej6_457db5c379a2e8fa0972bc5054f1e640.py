#Ordenar tres números
n1=int(input("Ingrese numero 1: "))
n2=int(input("Ingrese numero 2: "))
n3=int(input("Ingrese numero 3: "))
lista=[]
lista.append(n1)
lista.append(n2)
lista.append(n3)
lista.sort()

resultado=""
for i in range(len(lista)):
    resultado+= str(lista[i])+ ","

print(resultado[: len(resultado)-1])
          