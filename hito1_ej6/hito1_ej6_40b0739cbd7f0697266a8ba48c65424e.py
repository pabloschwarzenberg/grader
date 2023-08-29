#Ordenar tres números
print('Escribe un numero: ')
x = input()
x = int(x)

print('Escribe otro numero: ')
y= input()
y = int(y)

print('Escribe un ultimo numero: ')
z = input()
z = int(z)

lista = [x, y, z]
lista.sort()
print('La lista de numeros que escribiste ordenados de menor a mayor es la siguiente: ')
print(lista)