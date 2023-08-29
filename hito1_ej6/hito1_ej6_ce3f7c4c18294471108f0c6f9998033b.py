#Ordenar tres números
x = 0
lista = []
while x != 3:
    num = int(input("introduce un numero: "))
    lista.append(num)
    x += 1
lista.sort()
print(lista)

