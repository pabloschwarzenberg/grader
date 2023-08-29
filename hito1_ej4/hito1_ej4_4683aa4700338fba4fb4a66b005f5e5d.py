#Conversión de Decimal a Binario
def decimal_binario(numero):

    numero_int = numero.split('.')[0]
    numero_decimal = numero.split('.')[1]

    return str(bin(int(numero_int)))[2:] + str(bin(int(numero_decimal)))[2:]

decimal = str(float(input()))
print('resultado=' + decimal_binario(decimal))
