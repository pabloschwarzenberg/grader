def ordenar_numeros(a, b, c):
    numeros = [a, b, c]
    numeros.sort()
    numeros_ordenados = ", ".join(map(str, numeros))
    return numeros_ordenados

# Solicitar al usuario ingresar los tres números enteros
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
numero3 = int(input("Ingrese el tercer número entero: "))

# Llamar a la función para ordenar los números
numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)

# Imprimir el resultado
print("Números ordenados:", numeros_ordenados)
