#Ordenar tres números
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

numeros = [n1,n2,n3]
numeros.sort()

print(numeros[0],end=',')
print(numeros[1],end=',')
print(numeros[2])