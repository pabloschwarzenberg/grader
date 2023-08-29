#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    resultado = ", ".join(str(num) for num in numeros)
    return resultado

# Solicitar al usuario los números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Ordenar y mostrar los números
resultado_ordenado = ordenar_numeros(numero1, numero2, numero3)
print("Números ordenados: " + resultado_ordenado)
