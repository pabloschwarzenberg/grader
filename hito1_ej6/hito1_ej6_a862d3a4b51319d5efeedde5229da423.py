#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    # Crear una lista con los números
    numeros = [num1, num2, num3]

    # Ordenar la lista de menor a mayor
    numeros.sort()

    # Convertir los números ordenados a cadenas de texto
    numeros_texto = [str(num) for num in numeros]

    # Unir los números con comas y imprimir el resultado
    resultado = ", ".join(numeros_texto)
    print(resultado)

# Pedir al usuario que ingrese los números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar e imprimir los números
ordenar_numeros(num1, num2, num3)
