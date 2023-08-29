#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    # Crear una lista con los números ingresados
    numeros = [num1, num2, num3]

    # Ordenar la lista de menor a mayor
    numeros.sort()

    # Imprimir los números ordenados separados por comas
    print(*numeros, sep=",")


# Pedir al usuario que ingrese los números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Llamar a la función para ordenar e imprimir los números
ordenar_numeros(numero1, numero2, numero3)