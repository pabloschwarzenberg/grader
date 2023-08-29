def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  # Ordena los números de menor a mayor
    
    resultado = ','.join(str(num) for num in numeros)  # Crea una cadena separada por comas
    
    return resultado

# Solicitar al usuario ingresar los tres números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Llamar a la función e imprimir el resultado
resultado_ordenado = ordenar_numeros(num1, num2, num3)
print("Números ordenados:", resultado_ordenado)

   