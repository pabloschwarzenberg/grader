# Solicitar al usuario ingresar los números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Crear una lista con los números ingresados
numeros = [numero1, numero2, numero3]

# Ordenar la lista de menor a mayor
numeros.sort()

# Convertir los números a cadena y unirlos con comas
numeros_str = ', '.join(str(num) for num in numeros)

# Imprimir los números ordenados
print(numeros_str)
      