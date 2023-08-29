#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    binario = bin(numero)[2:]  
    print("Resultado =", binario)

numero_decimal = int(input("Ingrese un número decimal: "))

decimal_a_binario(numero_decimal)
     