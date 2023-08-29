#Ordenar tres números enteros de menor a mayor
def ordenar_numeros(n1, n2, n3):
    numeros = [n1, n2, n3]
    numeros.sort()  # Ordenar la lista de números de menor a mayor
    resultado = ", ".join(str(n) for n in numeros)  # Convertir los números en cadenas y unirlos con comas
    return resultado

# Obtener los números del usuario
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar e imprimir los números
resultado = ordenar_numeros(n1, n2, n3)
print("Números ordenados:", resultado)
      