def ordenar_numeros(num1, num2, num3):
    # Crear una lista con los números
    numeros = [num1, num2, num3]
    
    # Ordenar la lista de menor a mayor
    numeros.sort()
    
    # Convertir los números ordenados a cadenas de texto
    numeros_str = [str(num) for num in numeros]
    
    # Unir los números con comas y imprimir el resultado
    resultado = ", ".join(numeros_str)
    print(resultado)


# Solicitar los números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar y mostrar los números
ordenar_numeros(numero1, numero2, numero3)
      