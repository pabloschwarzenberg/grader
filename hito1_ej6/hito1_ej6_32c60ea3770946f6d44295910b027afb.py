#ordenar tres numeros 
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  # Ordena los números de menor a mayor

    # Imprime los números separados por comas
    print(", ".join(str(num) for num in numeros))

# Solicita al usuario ingresar los números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

# Llama a la función para ordenar e imprimir los números
ordenar_numeros(numero1, numero2, numero3)
