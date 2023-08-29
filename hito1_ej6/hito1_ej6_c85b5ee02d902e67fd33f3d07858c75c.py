numeros = []

for i in range(3):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)

numeros.sort()

resultado = ", ".join(map(str, numeros))
print("Los números ordenados de menor a mayor son:", resultado)

