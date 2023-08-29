def ordenar_numeros(num1, num2, num3):
    numeros_ordenados = sorted([num1, num2, num3])
    resultado = ','.join(map(str, numeros_ordenados))
    return resultado

# Solicitar los números al usuario
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Llamar a la función y mostrar el resultado
resultado_ordenado = ordenar_numeros(numero1, numero2, numero3)
print("Números ordenados de menor a mayor:", resultado_ordenado)

      