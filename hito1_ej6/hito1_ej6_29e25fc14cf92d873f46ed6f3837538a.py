#Ordenar tres números
lista = []
x=0

for i in range(3):
    n = int(input("Ingrese un numero: "))
    lista.append(n)
lista.sort()
str(lista)
print(lista[0],",",lista[1],",",lista[2])