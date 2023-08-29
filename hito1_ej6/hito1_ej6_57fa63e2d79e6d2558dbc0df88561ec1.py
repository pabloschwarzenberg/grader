#Ordenar 3 números

n1 = int(input('Escriba el primer número: '))
n2 = int(input('Escriba el segundo número: '))
n3 = int(input('Escriba el tercer número: '))

a = min(n1, n2, n3)
b = max(n1, n2, n3)
c = (n1 + n2 + n3) - a - b

print('Los números ordenados de menor a mayor quedan de la siguiente manera: {} , {} , {}'.format(a , c, b))