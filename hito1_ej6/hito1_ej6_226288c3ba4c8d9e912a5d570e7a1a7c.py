#Ordenar tres números
      def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]  # Creamos una lista con los números ingresados
    numeros.sort()  # Ordenamos la lista de menor a mayor

    resultado = ",".join(map(str, numeros))  # Convertimos los números a cadenas y los unimos con comas

    return resultado

# Pedimos al usuario que ingrese los números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Llamamos a la función para ordenar los números
resultado_ordenado = ordenar_numeros(num1, num2, num3)

# Imprimimos los números ordenados
print("Números ordenados de menor a mayor:", resultado_ordenado)