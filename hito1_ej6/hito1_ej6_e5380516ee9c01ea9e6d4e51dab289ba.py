# Solicitar al usuario que ingrese tres números enteros
numeros = []
for i in range(3):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)

# Ordenar los números de menor a mayor
numeros.sort()

# Crear una cadena con los números ordenados separados por comas
cadena_numeros = ", ".join(str(num) for num in numeros)

# Imprimir los números ordenados separados por comas
print("Los números ordenados de menor a mayor son:", cadena_numeros)
