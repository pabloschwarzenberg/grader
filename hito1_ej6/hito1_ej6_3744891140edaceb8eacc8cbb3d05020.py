#Ordenar tres números

lista = []
cantidad = 0

while(cantidad < 3):
    numeros = int(input("Ingrese un número entero: "))
    cantidad += 1
    lista.append(numeros)
lista.sort()

print(lista)