#Ordenar tres números

n1=int(input("Ingrese el primer número: "))
n2=int(input("Ingrese el segundo número: "))
n3=int(input("Ingrese el tercer número: "))

numeros=[n1,n2,n3]
numeros.sort()

print(numeros[0],",",numeros[1],",",numeros[2])