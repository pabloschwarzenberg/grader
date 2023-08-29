
def ordenar_numeros(a, b, c):
    numeros = [a, b, c]
    numeros.sort()  # Ordena la lista de números de menor a mayor
    
    # Imprime los números ordenados separados por comas
    print(", ".join(str(num) for num in numeros))


# Solicita al usuario ingresar los tres números enteros
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Llama a la función para ordenar y mostrar los números
ordenar_numeros(num1, num2, num3)
      