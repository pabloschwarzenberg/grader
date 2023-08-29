#Ordenar tres números
      # Función para ordenar los números
def ordenar_numeros(a, b, c):
    numeros = [a, b, c]
    numeros.sort()  # Ordena los números de menor a mayor
    return numeros

# Función principal
def main():
    # Solicitar los números al usuario
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    # Ordenar los números
    numeros_ordenados = ordenar_numeros(num1, num2, num3)

    # Imprimir los números ordenados
    print("Números ordenados:", ", ".join(map(str, numeros_ordenados)))

# Llamar a la función principal
main()
