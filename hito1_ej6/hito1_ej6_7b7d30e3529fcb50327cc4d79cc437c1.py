#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    # Crear una lista con los numeros ingresados
    numeros = [num1, num2, num3]

    # Ordenar la lista en orden ascendente
    numeros.sort()

    # Convertir la lista ordenada en una cadena separada por comas
    numeros_ordenados = ', '.join(map(str, numeros))

    # Imprimir los numeros ordenados
    print("Numeros ordenados de menor a mayor:", numeros_ordenados)


# Solicitar al usuario que ingrese los numeros
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

# Llamar a la funcion para ordenar los numeros e imprimir el resultado
ordenar_numeros(numero1, numero2, numero3)

  
     