#Conversión de Decimal a Binario
#Solicitar al usuario el número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

#Convertir el número decimal a binario
binario = bin(numero_decimal)[2:]  # [2:] para eliminar el prefijo "0b" del resultado binario

#Imprimir el resultado binario
print("resultado =", binario)