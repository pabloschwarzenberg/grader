#Ordenar tres números
lista = []
while len(lista) < 3:
    numero = int(input(' numero entero: '))
    lista.append(numero)

lista.sort()

print(lista[0],', ', lista[1], ', ', lista[2])
  