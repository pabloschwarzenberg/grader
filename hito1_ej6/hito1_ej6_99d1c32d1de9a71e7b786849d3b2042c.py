def ordenar_numeros(a, b, c):
    numeros = [a, b, c]
    numeros.sort()
    return numeros
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
numeros_ordenados = ordenar_numeros(a, b, c)
print(numeros_ordenados[0],",", numeros_ordenados[1],",", numeros_ordenados[2])