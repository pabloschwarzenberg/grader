def ordenar_numeros(num1, num2, num3):
    # Creamos una lista con los tres números
    numeros = [num1, num2, num3]
    
    # Ordenamos la lista de menor a mayor
    numeros.sort()
    
    # Convertimos los números a cadenas de texto y los unimos con comas
    numeros_str = ', '.join(str(num) for num in numeros)
    
    # Imprimimos los números ordenados
    print("Números ordenados de menor a mayor: " + numeros_str)

# Solicitamos al usuario que ingrese los números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Llamamos a la función para ordenar e imprimir los números
ordenar_numeros(numero1, numero2, numero3)
