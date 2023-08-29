#Conversión de Decimal a Binario
print("Ingrese número decimal: ")
numero_decimal = int(input(">>>"))

numero_binario = bin(numero_decimal)[2:]

print("resultado =", numero_binario)      