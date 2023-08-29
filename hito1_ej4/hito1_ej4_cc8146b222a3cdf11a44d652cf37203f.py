caracter = float(input("Ingresa un caracter: "))

caracter = int(caracter)
binario = bin(caracter)
binario = binario[2:]

print("resultado =",binario)