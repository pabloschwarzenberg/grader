#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    # Crear una lista con los números
    numeros = [num1, num2, num3]
    
    # Ordenar la lista de menor a mayor
    numeros.sort()
    
    # Convertir los números ordenados a cadena y unirlos con comas
    numeros_str = ", ".join(str(num) for num in numeros)
    
    # Imprimir los números ordenados
    print(numeros_str)

# Solicitar al usuario que ingrese los números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar y mostrar los números
ordenar_numeros(numero1, numero2, numero3)
      