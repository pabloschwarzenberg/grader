def ordenar_numeros(a, b, c):
    numeros = [a, b, c]  # Crear una lista con los números ingresados
    numeros.sort()  # Ordenar la lista de menor a mayor

    # Imprimir los números separados por comas
    numeros_ordenados = ', '.join(map(str, numeros))
    print(numeros_ordenados)

# Pedir al usuario que ingrese los números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar e imprimir los números
ordenar_numeros(numero1, numero2, numero3)

