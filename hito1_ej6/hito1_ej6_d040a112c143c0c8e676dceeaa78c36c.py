#Ordenar tres números
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))

numeros = [n1, n2, n3]
numeros.sort()

for i in range(len(numeros)):
print(numeros[i], end="/n")
if i != len(numeros) - 1:
print(",", end="/n")
