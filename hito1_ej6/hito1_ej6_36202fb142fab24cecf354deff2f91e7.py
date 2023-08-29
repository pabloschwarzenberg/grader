numeros = []

# Le agregamos 3 números
for i in range(3):
    numero = int(input("Introduce el número #{}: ".format(i + 1)))
    numeros.append(numero)

numeros.sort()
print(numeros)