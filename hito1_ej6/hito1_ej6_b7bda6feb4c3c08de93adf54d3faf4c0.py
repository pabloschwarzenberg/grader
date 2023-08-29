def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

numeros_ordenados = ordenar_numeros(num1, num2, num3)
resultado = ", ".join(str(num) for num in numeros_ordenados)

print("Números ordenados de menor a mayor:", resultado)