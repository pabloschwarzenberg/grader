#Ordenar tres números
lista = []
for i in range(1,4):
    a = int(input("Ingrese algún número entero para ordenar: "))
    lista.append(a)
print("Los números escogidos son: ", lista)
lista.sort()
print("Ordenados: ", lista)