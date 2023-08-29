def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros

# Solicitar los números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Ordenar los números
numeros_ordenados = ordenar_numeros(num1, num2, num3)

# Imprimir los números ordenados
print(",".join(str(num) for num in numeros_ordenados))
