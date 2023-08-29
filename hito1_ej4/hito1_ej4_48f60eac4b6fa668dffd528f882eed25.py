numero = int(input(" ingrese el numero que desea convertir en binario: "))
numeroArray = [int(d) for d in str(numero)]

binario = bin(numero)
print(" resultado = " + str(binario[2:]))