#Ordenar tres números
print('\nIngrese tres números:')

lista_n = []
n1 = int(input('\nNúmero 1: '))
lista_n.append(n1)
n2 = int(input('\nNúmero 2: '))
lista_n.append(n2)
n3 = int(input('\nNúmero 3: '))
lista_n.append(n3)
lista_n.sort()
print('\n')

print(lista_n[0], ', ', lista_n[1], ', ', lista_n[2])