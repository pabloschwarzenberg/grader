#Ordenar tres números

lista_numeros = []

num_1 = lista_numeros.append(int(input('Ingrese el primer número:\n')))
num_2 = lista_numeros.append(int(input('Ingrese el segundo número:\n')))
num_3 = lista_numeros.append(int(input('Ingrese el tercer número:\n')))

lista_numeros.sort()
print('Los números ordenados de menor a mayor son:\n', lista_numeros)