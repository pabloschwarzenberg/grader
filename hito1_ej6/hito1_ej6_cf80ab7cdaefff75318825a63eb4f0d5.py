#Ordenar tres números
  def ordenar_numeros(num1, num2, num3):
    # Crear una lista con los números ingresados
    numeros = [num1, num2, num3]
    
    # Ordenar la lista de menor a mayor
    numeros.sort()
    
    # Convertir la lista ordenada en una cadena separada por comas
    numeros_ordenados = ", ".join(str(num) for num in numeros)
    
    # Imprimir los números ordenados
    print("Números ordenados:", numeros_ordenados)


# Solicitar al usuario que ingrese los números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar y mostrar los números
ordenar_numeros(numero1, numero2, numero3)
