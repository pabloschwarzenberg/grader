#programa que recibe tres nùmeros enteros y los imprime en pantalla

def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    for i in range(len(numeros)):
        for j in range(len(numeros) - 1):
            if numeros[j] > numeros[j+1]:
                temp = numeros[j]
                numeros[j] = numeros[j+1]
                numeros[j+1] = temp
    return numeros

# Solicitar los tres números al usuario
num1 = int(input("Ingresa num1: "))
num2 = int(input("Ingresa num2: "))
num3 = int(input("Ingresa num3: "))

# Ordena los números
numeros_ordenados = ordenar_numeros(num1, num2, num3)

# Imprime los números ordenados separados por comas
print(f"Números ordenados de menor a mayor: {numeros_ordenados[0]}, {numeros_ordenados[1]}, {numeros_ordenados[2]}")
      