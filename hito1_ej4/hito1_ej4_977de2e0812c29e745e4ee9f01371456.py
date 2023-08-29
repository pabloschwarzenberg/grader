#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    if numero == 0:
        return '0'
    
    digitos_binarios = []
    
    while numero > 0:
        residuo = numero % 2
        digitos_binarios.append(str(residuo))
        numero = numero // 2
    
    digitos_binarios.reverse()
    resultado = ''.join(digitos_binarios)
    
    return resultado

numero_decimal = int(input("Ingresa un número decimal: "))
resultado_binario = decimal_a_binario(numero_decimal)
print("Resultado =", resultado_binario)
