#Ordenar tres numeros
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    numeros_ordenados = ','.join(map(str, numeros))
    return numeros_ordenados

# Solicitar los números al usuario
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Llamar a la función y mostrar el resultado
resultado = ordenar_numeros(numero1, numero2, numero3)
print("Números ordenados:", resultado)