#Ordenar tres números

numero=int(input())
lista=[]
lista.append(numero)
cont=1

while cont<3:
  numero=int(input())
  lista.append(numero)
  cont+=1

lista.sort()
print(lista)    