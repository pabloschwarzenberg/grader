#Ordenar tres números

lista = []
while len(lista) != 3:
    x = int(input("ingrese un numero: "))
    lista.append(x)
lista.sort()
print(lista)