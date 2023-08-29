numeros = []

for i in range(3):
    num = int(input("Introduce un número entero: "))
    numeros.append(num)

numeros.sort()

for i in range(3):
    if i == 2:
        print(numeros[i])
    else:
        print(numeros[i], end=", ")