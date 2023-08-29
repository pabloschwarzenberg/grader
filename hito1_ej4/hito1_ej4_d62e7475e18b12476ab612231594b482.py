#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    
    resultado = ""
    
    while numero > 0:
        resultado = str(numero % 2) + resultado
        numero //= 2
    
    return resultado

numero_decimal = int(input("Ingrese un número decimal: "))
resultado_binario = decimal_a_binario(numero_decimal)
print("resultado=" + resultado_binario)





