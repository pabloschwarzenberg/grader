#Conversión de Decimal a Binario

def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return binario

# Solicitar al usuario que ingrese el número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Llamar a la función y mostrar el resultado
resultado_binario = decimal_a_binario(numero_decimal)
print("resultado=" + resultado_binario)
