def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

numeros_ordenados = ordenar_numeros(num1, num2, num3)

print("Los números ordenados de menor a mayor son:", end=" ")
for i in range(len(numeros_ordenados)):
    if i == len(numeros_ordenados) - 1:
        print(numeros_ordenados[i])
    else:
        print(numeros_ordenados[i], end=", ")