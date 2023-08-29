#Ordenar tres números
lista = []

for i in range (3):
    num=int(input("Ingrese un numero: "))
    lista.append(num)

lista.sort()

print(lista[0],lista[1],lista[2],sep=",")