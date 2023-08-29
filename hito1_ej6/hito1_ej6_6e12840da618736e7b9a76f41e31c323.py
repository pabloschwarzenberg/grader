def ordenar_numeros(num1, num2, num3):
    # Crear una lista con los tres números
    numeros = [num1, num2, num3]
    
    # Ordenar la lista de menor a mayor
    numeros.sort()
    
    # Convertir los números a cadenas de caracteres
    numeros_str = [str(num) for num in numeros]
    
    # Unir los números en una cadena separada por comas
    numeros_ordenados = ", ".join(numeros_str)
    
    # Imprimir los números ordenados
    print("Números ordenados:", numeros_ordenados)

# Solicitar al usuario que ingrese los números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar los números e imprimirlos
ordenar_numeros(num1, num2, num3)



      