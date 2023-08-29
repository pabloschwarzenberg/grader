#Ordenar tres números

lista=[]
for i in range(1,4):
  numero = int(input("Ingrese número {0}: ".format(i)))
  lista.append(numero)
  lista.sort()
print(lista)
