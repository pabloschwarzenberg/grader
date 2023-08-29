#Conversión de Decimal a Binario
def decimal(decimal):
    binario = bin(decimal)[2:]
    return binario

numero_decimal = int(input("Ingrese un número decimal: "))
resultado_binario = decimal(numero_decimal)
print("resultado=", resultado_binario)      
      