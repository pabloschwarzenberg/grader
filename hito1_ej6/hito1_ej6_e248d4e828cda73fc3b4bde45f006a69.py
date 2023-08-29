#En este programa se meten a la consola numeros enteros y los imprime de menor a mayor 
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    numeros_ordenados = ", ".join(str(num) for num in numeros)
    return numeros_ordenados

# Pedir al usuario que ingrese los números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar los números
numeros_ordenados = ordenar_numeros(num1, num2, num3)

# Imprimir los números ordenados
print("Los números ordenados de menor a mayor son:", numeros_ordenados)
