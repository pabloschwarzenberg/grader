#Ordenar tres números
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

# Ordenar los números de menor a mayor
ordenados = sorted([a, b, c])

# Imprimir los números ordenados
print(ordenados[0], ordenados[1], ordenados[2], sep=", ")
