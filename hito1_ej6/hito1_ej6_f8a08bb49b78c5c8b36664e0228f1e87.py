#Ordenar tres números
n = int(input("ingrese un numero: "))
m = int(input("ingrese un numero: "))
b = int(input("ingrese un numero: "))
numeros = list(n,m,b)
numeros.sort()
print(numeros,sep= ",")