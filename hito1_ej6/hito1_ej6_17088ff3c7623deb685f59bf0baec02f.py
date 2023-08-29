numeros = []

for i in range(3):
    numero = int(input("Ingresa un número entero: "))
    numeros.append(numero)

numeros.sort()

numeros_ordenados = ','.join(str(num) for num in numeros)
print(numeros_ordenados)



