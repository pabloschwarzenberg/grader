#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    resultado = ", ".join(str(num) for num in numeros)
    return resultado

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

resultado_ordenado = ordenar_numeros(num1, num2, num3)

print("Números ordenados de menor a mayor:", resultado_ordenado)
