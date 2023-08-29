#Ordenar tres números
def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    numeros_ordenados = ", ".join(map(str, numeros))
    return numeros_ordenados

# Solicitar los números al usuario
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))

# Ordenar y mostrar los números
numeros_ordenados = ordenar_numeros(n1, n2, n3)
print("Números ordenados de menor a mayor:", numeros_ordenados)
      