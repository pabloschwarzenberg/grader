def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    numeros_str = [str(num) for num in numeros]
    numeros_ordenados = ", ".join(numeros_str)
    print("Números ordenados de menor a mayor:", numeros_ordenados)

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

ordenar_numeros(num1, num2, num3)
