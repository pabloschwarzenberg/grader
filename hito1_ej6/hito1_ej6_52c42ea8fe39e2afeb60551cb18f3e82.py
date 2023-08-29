#Ordenar tres números
def ordenar_numeros(a, b, c):
    numeros = [a, b, c]
    numeros.sort()
    numeros_ordenados = ', '.join(map(str, numeros))
    return numeros_ordenados

# Solicitar los tres números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar los números
resultado = ordenar_numeros(num1, num2, num3)

# Imprimir los números ordenados
print("Números ordenados:", resultado)
