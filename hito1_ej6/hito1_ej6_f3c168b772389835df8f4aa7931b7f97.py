#Ordenar tres números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Creamos una lista con los números ingresados
numeros = [num1, num2, num3]

# Ordenamos la lista de menor a mayor
numeros.sort()

# Imprimimos los números separados por comas
print("Los números ordenados son:", ", ".join(map(str, numeros)))
