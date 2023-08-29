def ordenar_numeros(a, b, c):
    numeros = [a, b, c]
    numeros.sort()
    numeros_str = [str(num) for num in numeros]
    numeros_ordenados = ", ".join(numeros_str)
    print("Números ordenados de menor a mayor:", numeros_ordenados)

# Ejemplo de uso
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

ordenar_numeros(numero1, numero2, numero3)
