num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

numeros = [num1, num2, num3]
numeros.sort()

ordenados = ""
for i in range(len(numeros)):
    ordenados += str(numeros[i])
    if i < len(numeros) - 1:
        ordenados += ", "

print(ordenados)
