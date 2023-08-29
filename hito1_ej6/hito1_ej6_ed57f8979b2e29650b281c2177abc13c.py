def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  # Ordena la lista de números de menor a mayor

    # Imprime los números separados por comas
    resultado = ",".join(str(num) for num in numeros)
    print(resultado)

# Ejemplo de uso
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

ordenar_numeros(numero1, numero2, numero3)
