numeros = []
for i in range(3):
    numero = int(input("Ingrese el número {}: ".format(i + 1)))
    numeros.append(numero)

numeros.sort()  # Ordena la lista de números de menor a mayor

numeros_ordenados = ", ".join(str(numero) for numero in numeros)  # Convierte y une los números en una cadena separada por comas

print(numeros_ordenados)
