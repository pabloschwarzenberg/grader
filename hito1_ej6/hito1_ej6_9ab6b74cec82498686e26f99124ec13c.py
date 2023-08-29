numeros = []

for i in range(3):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)

numeros.sort()

print("Los números ordenados de menor a mayor son:", end=" ")

for numero in numeros:
    print(numero, end=", ")