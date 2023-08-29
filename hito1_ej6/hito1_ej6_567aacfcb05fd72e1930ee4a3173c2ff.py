#Ordenar tres números

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))
numero3 = int(input("Ingrese otro número: "))

numeros = numero1, numero2, numero3
numeros = list(numeros)

numeros.sort()

print(numeros)