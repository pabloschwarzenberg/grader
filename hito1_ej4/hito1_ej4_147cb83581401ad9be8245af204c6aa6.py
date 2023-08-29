numero_decimal = int(input("Ingrese un número decimal: "))

resultado_binario = bin(numero_decimal)[2:]  # [2:] para eliminar el prefijo '0b' de la representación binaria

print("Resultado =", resultado_binario)
   