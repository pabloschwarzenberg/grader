#Ordenar tres números

primero = int(input("Ingresa el primer número: "))
segundo = int(input("Ingresa el segundo número: "))
tercero = int(input("Ingresa el tercer número: "))
numeros_ordenados = sorted([primero, segundo, tercero])
print(numeros_ordenados[0], numeros_ordenados[1], numeros_ordenados[2], sep=",")