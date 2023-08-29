#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    resultado = ",".join(str(num) for num in numeros)
    return resultado

# Solicitar al usuario los tres números enteros
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

# Ordenar y mostrar los números
numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)
print("Números ordenados:", numeros_ordenados)

