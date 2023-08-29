#Conversión de Decimal a Binario

def decimal_a_binario(decimal):
    if decimal == 0:
        return '0'
    elif decimal < 0:
        return '-' + decimal_a_binario(abs(decimal))
    else:
        bits = []
        while decimal > 0:
            bits.append(str(decimal % 2))
            decimal //= 2
        bits.reverse()
        return ''.join(bits)

#Pedir un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

#Conversión decimal a binario
resultado = decimal_a_binario(numero_decimal)

#Resultado
print("resultado =", resultado)