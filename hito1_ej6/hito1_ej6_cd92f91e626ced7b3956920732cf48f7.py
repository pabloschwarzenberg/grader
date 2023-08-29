#Ordenar tres números
def ordenar_numeros(a, b, c):
    # Crear una lista con los tres números
    numeros = [a, b, c]
    
    # Ordenar la lista de menor a mayor
    numeros.sort()
    
    # Imprimir los números separados por comas
    print(','.join(str(num) for num in numeros))


# Solicitar al usuario que ingrese los tres números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar e imprimir los números
ordenar_numeros(numero1, numero2, numero3)
