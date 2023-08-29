#Ordenar tres números

X = int(input('Escriba el primer numero: '))
Y = int(input('Escriba el segundo numero: '))
Z = int(input('Escriba el tercer numero: '))

a = min(X, Y, Z)
c = max(X, Y , Z)
b = (X + Y + Z) - a - c
print(a , ", ", b, ", ", c)