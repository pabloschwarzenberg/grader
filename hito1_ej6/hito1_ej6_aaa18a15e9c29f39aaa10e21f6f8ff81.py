#Ordenar tres números
def ordenar_numeros(a, b, c):
    numeros = [a, b, c]
    numeros.sort()
    resultado = ",".join(str(num) for num in numeros)
    return resultado

# Solicitar los tres números al usuario
numero1 = int(input("Ingresa el primer número entero: "))
numero2 = int(input("Ingresa el segundo número entero: "))
numero3 = int(input("Ingresa el tercer número entero: "))

# Ordenar los números y mostrar el resultado
resultado_ordenado = ordenar_numeros(numero1, numero2, numero3)
print("Números ordenados de menor a mayor:", resultado_ordenado)
      