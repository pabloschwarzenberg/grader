#Ordenar tres números
     def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    numeros_ordenados = ','.join(map(str, numeros))
    return numeros_ordenados

# Solicitar los tres números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar e imprimir los números
numeros_ordenados = ordenar_numeros(num1, num2, num3)
print("Números ordenados: " + numeros_ordenados)
